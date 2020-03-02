from smile.common import Experiment, Wait, Parallel, KeyPress,UntilDone,\
                         Serial, Label, Log
from smile.video import *
from smile.moving_dots import MovingDots
from smile.state import UntilDone, Meanwhile, Wait, Loop, Debug
from smile.scale import scale as s
from config import *
from instructmovingdots import *

from gen_movingdots import *

"""Chuiwen's experimental version"""

exp = Experiment(background_color=[0.5,0.5,0.5,0.5] )#"gray")

Wait(.1)

Instruct(config = config, lang="E")

Wait(.1)

with Loop(blocks) as block:
    with Loop(block.current) as ds: #dots set
        fixation_point = Label(text="+",duration=0.75, 
                                font_size = 80, bold = False, 
                                color = [0,0,0,1])
        with Parallel():
            md_white = MovingDots(radius=s(300), scale=s(2.5), color="white", num_dots=250,
                                motion_props=ds.current['motion_props'])
            md_black = MovingDots(radius=s(300), scale=s(2.5), color="black", num_dots=250,
                                motion_props=ds.current['motion_props'])
        with UntilDone():
            Wait(until=fixation_point.disappear_time)
            kp=KeyPress(keys=["F","J"],duration=3., correct_resp=ds.current['CR'],
                        base_time = fixation_point.disappear_time['time'])
        Log(ds.current,
            name="trial_data", 
            pressed=kp.pressed,
            rt=kp.rt,
            base_time=kp.base_time,
            correct=kp.correct,
            appear_time=md_white.appear_time,
            disappear_time=md_white.disappear_time,
            )
    rest = Label(text='Have a rest...\n'+
                        'press [b]SPACEBAR[/b] to continue.',
                markup=True, halign='center', text_size=(s(s(config['INST_RADIUS'])*4.5), None),
                font_size=s(config['INST_FONT_SIZE'])*2)
    with UntilDone():
            # Wait(until=rest.appear_time)
            kp=KeyPress(keys=["SPACEBAR"])


with UntilDone():
    KeyPress(keys=['Q'])


exp.run(trace=False)
