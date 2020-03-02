# -*- coding: utf-8 -*-

from smile.common import *
from smile.scale import scale as s

"""Chuiwen's experimental version"""

# Text for instructions
top_text = {'E':'Your goal is to determine the direction that\n' +
                '[i]MOST[/i] of the dots are moving.\n' +
                'Please respond quickly and accurately.',
            'S':'Su objetivo es determinar la dirección que la\n' +
                '[b]MAYORÍA[/b] de los puntos se están moviendo.\n' +
                'Por favor responda con rapidez y precisión.',
            'P':'Seu objetivo é determinar a direção em que' +
                '[b]A MAIOR PARTE[/b] dos pontos está se movendo.' +
                'Por favor responda rápida e diretamente.'}

def bottom_text(config, left=True, lang="E"):
    if not left:
        if lang == "E":
            value_str = 'Press the [b]J[/b]' + \
                        ' if the [b]DIRECTION OF THE DOTS[/b] is ' + \
                        '[b]TO THE RIGHT[/b]'
        # elif lang == "S":
        #     value_str = 'Press the [b]{0}[/b]'.format(config.RESP_KEYS[-1]) + \
        #                 ' if the [b]DIRECTION OF THE DOTS[/b] is ' + \
        #                 '[b]TO THE RIGHT[/b]'
        # elif lang == "P":
        #     value_str = 'Press the [b]{0}[/b]'.format(config.RESP_KEYS[-1]) + \
        #                 ' if the [b]DIRECTION OF THE DOTS[/b] is ' + \
        #                 '[b]TO THE RIGHT[/b]'
    else:
        if lang == "E":
            value_str = 'Press the [b]F[/b] ' + \
                        'if the [b]DIRECTION OF THE DOTS[/b] is ' + \
                        '[b]TO THE LEFT[/b]'
        # if lang == "S":
        #     value_str = 'Press the [b]{0}[/b] '.format(config.RESP_KEYS[0]) + \
        #                 'if the [b]DIRECTION OF THE DOTS[/b] is ' + \
        #                 '[b]TO THE LEFT[/b]'
        # if lang == "P":
        #     value_str = 'Press the [b]{0}[/b] '.format(config.RESP_KEYS[0]) + \
        #                 'if the [b]DIRECTION OF THE DOTS[/b] is ' + \
        #                 '[b]TO THE LEFT[/b]'

    # eval and return the str
    return value_str


@Subroutine

def Instruct(self, config, lang="E"):
    cont_key_str = 'SPACE'
    print(cont_key_str)
    with If(lang=="E"):
        self.top_text = 'Your goal is to determine the direction that\n [i]MOST[/i] of the dots are moving.\n Please respond quickly and accurately.'# Ref.object(top_text)['E']
        # self.tap_text_M = 'Tap [b]the screen[/b] when you ' + 'are ready to begin the block.'
        self.tap_text_C = 'Press [b]%s[/b] when you are ready to begin the block.'%(cont_key_str)


    # handle the reverse mapping
    with Parallel():
        Label(text=self.top_text,
              markup=True, halign='center', text_size=(s(s(config['INST_RADIUS'])*4.5), None),
              bottom=self.exp.screen.center_y + s(config['INST_RADIUS']) + s(60),
              font_size=s(config['INST_FONT_SIZE'])*2)
        md_l_w = MovingDots(color='white', scale=s(2),
                          num_dots=config['NUM_DOTS'], radius=s(config['INST_RADIUS']),
                          coherence=config['COHERENCES'],
                          direction=180, lifespan=config['INST_LIFESPAN'],
                          center_y=self.exp.screen.center_y + s(45),
                          lifespan_variance=config['INST_LIFESPAN_VAR'], speed=s(config['INST_SPEED']),
                          right=self.exp.screen.center_x - s(100))
        md_l_b = MovingDots(color='black', scale=s(2),
                          num_dots=config['NUM_DOTS'], radius=s(config['INST_RADIUS']),
                          coherence=config['COHERENCES'],
                          direction=180, lifespan=config['INST_LIFESPAN'],
                          center_y=self.exp.screen.center_y + s(45),
                          lifespan_variance=config['INST_LIFESPAN_VAR'], speed=s(config['INST_SPEED']),
                          right=self.exp.screen.center_x - s(100))
        md_r_w = MovingDots(color='white', scale=s(2),
                          num_dots=config['NUM_DOTS'], radius=s(config['INST_RADIUS']),
                          coherence=config['COHERENCES'],
                          direction=0, lifespan=config['INST_LIFESPAN'],
                          center_y=self.exp.screen.center_y + s(45),
                          lifespan_variance=config['INST_LIFESPAN_VAR'], speed=s(config['INST_SPEED']),
                          right=self.exp.screen.center_x + s(500))
        md_r_b = MovingDots(color='black', scale=s(2),
                          num_dots=config['NUM_DOTS'], radius=s(config['INST_RADIUS']),
                          coherence=config['COHERENCES'],
                          direction=0, lifespan=config['INST_LIFESPAN'],
                          center_y=self.exp.screen.center_y + s(45),
                          lifespan_variance=config['INST_LIFESPAN_VAR'], speed=s(config['INST_SPEED']),
                          right=self.exp.screen.center_x + s(500))
        lt = Label(text=Ref(bottom_text, config, True, lang),
              markup=True, halign='left',
              text_size=(s(config['INST_RADIUS'])*1.9, None),
              left_top=(self.exp.screen.center_x - (2*s(config['INST_RADIUS'])) - s(50),
                          self.exp.screen.center_y - (s(config['INST_RADIUS']))),
              font_size=s(config['INST_FONT_SIZE']))
        Label(text=Ref(bottom_text, config, False, lang),
              markup=True, halign='right',
              text_size=(s(config['INST_RADIUS'])*1.9, None),
              right_top=(self.exp.screen.center_x + 2*s(config['INST_RADIUS']) + s(50),
                          self.exp.screen.center_y - s(config['INST_RADIUS'])),
              font_size=s(config['INST_FONT_SIZE']))
       
        Label(text=self.tap_text_C,
                font_size=s(config['INST_FONT_SIZE']*1.5),
                top=lt.bottom - s(80),
                markup=True, halign='center')

    with UntilDone():
        kp=KeyPress(keys=["SPACEBAR"])
