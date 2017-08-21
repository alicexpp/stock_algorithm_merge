# fc_area_recommend_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def move_01(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==1:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_02(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==2:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_03(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==3:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_04(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==4:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_05(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==5:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_06(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==6:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_07(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==7:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_area_recommend')
  
  fc_rule.fc_rule('move_01', This_rule_base, move_01,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p0'),
       contexts.variable('p1'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p1'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_02', This_rule_base, move_02,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p1'),
       contexts.variable('p2'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p2'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_03', This_rule_base, move_03,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p2'),
       contexts.variable('p3'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p3'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_04', This_rule_base, move_04,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p3'),
       contexts.variable('p4'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p4'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_05', This_rule_base, move_05,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p4'),
       contexts.variable('p5'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p5'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_06', This_rule_base, move_06,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p5'),
       contexts.variable('p6'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p6'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_07', This_rule_base, move_07,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p6'),
       contexts.variable('p7'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p7'),
     contexts.variable('status'),))


Krb_filename = '..\\fc_area_recommend.krb'
Krb_lineno_map = (
    ((13, 17), (5, 5)),
    ((18, 22), (6, 6)),
    ((23, 23), (7, 7)),
    ((24, 27), (9, 9)),
    ((36, 40), (15, 15)),
    ((41, 45), (16, 16)),
    ((46, 46), (17, 17)),
    ((47, 50), (19, 19)),
    ((59, 63), (24, 24)),
    ((64, 68), (25, 25)),
    ((69, 69), (26, 26)),
    ((70, 73), (28, 28)),
    ((82, 86), (33, 33)),
    ((87, 91), (34, 34)),
    ((92, 92), (35, 35)),
    ((93, 96), (37, 37)),
    ((105, 109), (42, 42)),
    ((110, 114), (43, 43)),
    ((115, 115), (44, 44)),
    ((116, 119), (46, 46)),
    ((128, 132), (51, 51)),
    ((133, 137), (52, 52)),
    ((138, 138), (53, 53)),
    ((139, 142), (55, 55)),
    ((151, 155), (60, 60)),
    ((156, 160), (61, 61)),
    ((161, 161), (62, 62)),
    ((162, 165), (64, 64)),
)
