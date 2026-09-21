# DGD Arcade backend.
#
# Node 24 runs the TypeScript directly — there is no build step and no
# transpiled output to keep in sync with the source.
FROM node:24-slim

ENV NODE_ENV=production
WORKDIR /app

# Dependencies first, so a source change does not re-resolve the tree.
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY src ./src
COPY data/bank ./data/bank

# The SQLite file and its WAL live here. Mount a volume at /app/data or every
# redeploy starts the players, XP and streaks from nothing.
VOLUME ["/app/data"]

EXPOSE 8787

# The container is unhealthy until the bank has parsed and the database has
# opened, which is what /healthz reports.
HEALTHCHECK --interval=30s --timeout=4s --start-period=10s --retries=3 \
  CMD node -e "fetch('http://127.0.0.1:'+(process.env.PORT||8787)+'/healthz').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

CMD ["node", "src/index.ts"]
