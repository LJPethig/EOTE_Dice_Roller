"""
All dice faces as tuples
die face[0] == filename of die face image
die face[1] == effect of die face, easier than using regex to extract effect from die face[0]
"""

boost_die_d6 = [('Boost-', ''), ('Boost-', ''), ('Boost-S', 'S'), ('Boost-SA', 'SA'), ('Boost-AA', 'AA'),
                ('Boost-A', 'A')]

setback_die_d6 = [('Setback-', ''), ('Setback-', ''), ('Setback-F', 'F'), ('Setback-F', 'F'), ('Setback-T', 'T'),
                  ('Setback-T', 'T')]

ability_die_d8 = [('Green-', ''), ('Green-S', 'S'), ('Green-S', 'S'), ('Green-SS', 'SS'), ('Green-A', 'A'),
                  ('Green-A', 'A'), ('Green-SA', 'SA'), ('Green-AA', 'AA')]

proficiency_die_d12 = [('Yellow-', ''), ('Yellow-S', 'S'), ('Yellow-S', 'S'), ('Yellow-SS', 'SS'),
                       ('Yellow-SS', 'SS'), ('Yellow-A', 'A'), ('Yellow-SA', 'SA'),
                       ('Yellow-SA', 'SA'), ('Yellow-SA', 'SA'), ('Yellow-AA', 'AA'), ('Yellow-AA', 'AA'),
                       ('Yellow-X', 'XS')]

difficulty_die_d8 = [('Purple-', ''), ('Purple-F', 'F'), ('Purple-FF', 'FF'), ('Purple-T', 'T'), ('Purple-T', 'T'),
                     ('Purple-T', 'T'), ('Purple-TT', 'TT'), ('Purple-FT', 'FT')]

challenge_die_d12 = [('Red-', ''), ('Red-F', 'F'), ('Red-F', 'F'), ('Red-FF', 'FF'), ('Red-FF', 'FF'), ('Red-T', 'T'),
                     ('Red-T', 'T'), ('Red-FT', 'FT'), ('Red-FT', 'FT'), ('Red-TT', 'TT'), ('Red-TT', 'TT'),
                     ('Red-D', 'DF')]

force_die_d12 = [('Force-B', 'B'), ('Force-B', 'B'), ('Force-B', 'B'), ('Force-B', 'B'), ('Force-B', 'B'),
                 ('Force-B', 'B'), ('Force-BB', 'BB'), ('Force-W', 'W'), ('Force-W', 'W'), ('Force-WW', 'WW'),
                 ('Force-WW', 'WW'), ('Force-WW', 'WW')]
