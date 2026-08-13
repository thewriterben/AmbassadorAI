"""Nevada — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Nevada'

CAMPUSES = [{'state': 'Nevada',
  'name': 'University of Nevada, Las Vegas',
  'city': 'Las Vegas, NV',
  'type': 'Public (NSHE)',
  'tier': 'C — Opportunistic',
  'access': 1,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Fri Aug 28, 2026 (last day to add online / full refund)',
  'fallbreak': 'Fri Oct 30 (Nevada Day); Wed Nov 11 (Veterans Day)',
  'thanksgiving': 'Nov 26–27, 2026 (reopens Nov 30)',
  'lastclass': 'Sat Dec 5, 2026 (study week from Nov 30)',
  'finals': 'Dec 7–12, 2026',
  'cal_url': 'https://www.unlv.edu/students/academic-calendar',
  'cal_status': 'CONFIRMED',
  'fair': 'Fall Involvement Fair',
  'fair_date': 'Wed Sep 2, 2026, 10am–2pm — Academic Mall and surrounding areas (Alumni Amphitheatre, Pida Plaza, '
               'Pioneer Lawn, WRI Lawn). CONFIRMED.',
  'fair_outside': "⚠ NO — and the prohibition is explicit: 'No organization may sell products, recruit for job "
                  "openings, or PROMOTE A BUSINESS.' DGD cannot table here, and cannot have a club table on its "
                  'behalf for promotional purposes.',
  'fair_cost': 'None mentioned',
  'fair_deadline': 'Registration opened Fri Aug 7, 2026; no closing date published',
  'fair_url': 'https://www.unlv.edu/sia/student-orgs/involvement-fair',
  'policy': 'Guidelines for Scheduling University Facilities (NSHE / Board of Regents)',
  'policy_url': 'https://www.unlv.edu/campuslife/scheduling-guidelines',
  'policy_key': "MOST EXPLICIT COMMERCIAL BAN IN NEVADA. 'COMMERCIAL ACTIVITY (SALES, MARKETING, ADVERTISING) BY "
                "NON-UNIVERSITY ENTITIES IS FORBIDDEN ON THE UNLV CAMPUS' except in designated locations: Thomas & "
                'Mack Center, Barrick Museum, Performing Arts Center, McDermott Complex, Student Union, and specific '
                "outdoor areas. Non-university users pay full rates and must carry insurance with 'combined single "
                "limits of liability of at least $1,000,000' naming the Board of Regents as additional insured, plus "
                'a hold-harmless/indemnification agreement. Non-profits must be county-licensed with federal '
                "tax-exempt status. External sponsors may support events but 'cannot create activity that is "
                "essentially commercial'; sponsors may distribute free samples only during events in reserved "
                'spaces. Free speech areas (leafletting and signature gathering only): Academic Mall, Carol Harter '
                'Classroom Building Complex Walkway, East/West Mall.',
  'sponsor_required': 'Sponsorship cannot cure a commercial purpose',
  'clubs': [('NOT ENUMERATED',
             'The UNLV Involvement Center directory is JavaScript-rendered. Search: blockchain, crypto, bitcoin, '
             'Web3, fintech, investment, finance, economics, entrepreneurship, ACM, data science, FMA. DO NOT ASSUME '
             'a blockchain club exists.',
             'https://involvementcenter.unlv.edu/organizations')],
  'faculty': [('Student Involvement & Activities',
               'Office',
               '',
               'involvement@unlv.edu · 702-895-5631',
               'https://www.unlv.edu/sia/student-orgs/involvement-fair'),
              ('(Faculty)',
               'NOT CONFIRMED. Look up at Lee Business School Finance dept and Computer Science dept.',
               '',
               '',
               'https://www.unlv.edu/business')],
  'courses': [('—', 'UNVERIFIED.', 'https://catalog.unlv.edu/')],
  'events': [('Fall Involvement Fair',
              'Wed Sep 2, 2026 — but business promotion is banned',
              'https://www.unlv.edu/sia/student-orgs/involvement-fair')],
  'play': 'DEPRIORITIZE. UNLV combines the most explicit non-university commercial ban in Nevada with an involvement '
          'fair that specifically prohibits promoting a business — closing both the direct and the club-proxy routes '
          'in a single stroke. The only lawful presence is leafletting in a designated free-speech area with '
          'non-commercial material. Not worth the drive from anywhere in your footprint.',
  'gaps': ['Club directory (JS-rendered)',
           'Any blockchain/fintech faculty',
           'Catalog courses',
           'Whether any designated venue would accept a crypto vendor']},
 {'state': 'Nevada',
  'name': 'University of Nevada, Reno',
  'city': 'Reno, NV',
  'type': 'Public (NSHE)',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Fri Aug 28 (without instructor approval); Wed Sep 2, 2026 (with permission)',
  'fallbreak': 'No discrete fall break; Fri Oct 30 (Nevada Day) and Wed Nov 11 (Veterans Day)',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': 'Wed Dec 16, 2026 (instruction ends)',
  'finals': 'Dec 10–16, 2026',
  'cal_url': 'https://www.unr.edu/admissions/records/academic-calendar/future-terms',
  'cal_status': 'CONFIRMED — ⚠ but the source rendered commencement as 12/5/26, which precedes finals. Treat '
                'end-of-term dates as UNVERIFIED.',
  'fair': 'ASUN Club Fair',
  'fair_date': 'UNVERIFIED — Fall 2026 date not published. Recurs each fall and spring, early in the semester.',
  'fair_outside': 'UNVERIFIED — but see policy: off-campus groups are barred from indoor tabling',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://events.unr.edu/event/asun_club_fair',
  'policy': 'Joe Crowley Student Union (JCSU) Tabling Procedures; UAM 5,302 and 5,305',
  'policy_url': 'https://www.unr.edu/union/event-services/tabling',
  'policy_key': "'Any department or recognized student organization (ASUN/GSA) is able to make reservations.' ⚠ "
                "'OFF-CAMPUS ORGANIZATIONS PROHIBITED INDOORS' — the 7 indoor spots on the 2nd/3rd floors are closed "
                "to outside entities. Off-campus groups 'must contact the team directly for special arrangements' — "
                "no self-serve path. OUTDOOR: 15 spots, 10'x10', one table + up to three chairs, small speakers "
                'allowed. Book 3 business days ahead via Lounge; max 5 active bookings per group; a representative '
                "'must be physically present at the tabling spot for the duration'; daily check-in at the "
                "Information Center; NO SOLICITING IN WALKWAYS. ⚠ NOTE: UAM 1,620 'Solicitation Procedures' governs "
                'FUNDRAISING/DEVELOPMENT (gift solicitation via the Foundation), NOT third-party commercial '
                'solicitation — DO NOT CITE IT as the vendor policy. The operative policies are UAM 5,302 (Use of '
                'University Space) and 5,305 (Posting, Distributing and Exhibiting) — CONTENTS NOT RETRIEVED.',
  'sponsor_required': 'Special arrangement with JCSU Event Services',
  'clubs': [('NOT ENUMERATED',
             'Directory is JS-rendered. Engineering-specific list available separately.',
             'https://unr.campuslabs.com/engage/organizations')],
  'faculty': [('JCSU Event Services',
               'Office',
               'Joe Crowley Student Union',
               'csures@unr.edu · (775) 682-7402',
               'https://www.unr.edu/union/event-services/tabling'),
              ('Center for Student Engagement',
               'Office',
               '',
               '',
               'https://www.unr.edu/student-engagement/forms-policies-data/policies')],
  'courses': [('—', 'UNVERIFIED.', 'https://catalog.unr.edu/')],
  'events': [('ASUN Club Fair', 'Fall 2026 date UNVERIFIED', 'https://events.unr.edu/event/asun_club_fair')],
  'play': 'UNR is materially more open than UNLV — outdoor tabling exists with a defined 3-business-day booking '
          "process and off-campus groups can request 'special arrangements' rather than being flatly banned. Call "
          'csures@unr.edu / (775) 682-7402 and ask what a special arrangement costs. But READ UAM 5,302 and 5,305 '
          'FIRST — those are the operative policies and neither was retrievable. Reno is also the most isolated stop '
          'in your footprint; only worth it bundled with a Sacramento or Bay Area leg you have not scoped.',
  'gaps': ['⚠ UAM 5,302 and 5,305 contents — the operative policies',
           'End-of-term date inconsistency',
           'Club Fair Fall 2026 date',
           'Club roster',
           'Faculty']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-09-02',
  'Sep 2, 2026',
  'UNLV',
  'Fall Involvement Fair, 10am–2pm, Academic Mall',
  "⚠ 'No organization may sell products, recruit for job openings, or promote a business.' DGD cannot table.",
  'https://www.unlv.edu/sia/student-orgs/involvement-fair',
  'involvement@unlv.edu')]
