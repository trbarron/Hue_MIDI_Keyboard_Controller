import pygame
import pygame.midi
import pprint
from phue import Bridge

b = Bridge('10.0.0.224')
b.connect()
lights = b.lights

pygame.init()
pygame.fastevent.init()
pygame.midi.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post
pLight = 3 #Default light # to 3 (all)
input_id = pygame.midi.get_default_input_id()
newSetting = False
saveStruct = [[[253 for w in xrange(3)] for q in xrange(3)] for u in xrange(47)]
for u in xrange(47):
        for l in xrange(3):
                saveStruct[u][l][1] = u*702
print "starting"

going = True
i = pygame.midi.Input( input_id )
while going:

        if i.poll():
                midi_events = i.read(1)
                #print(midi_events[0][0])

                if (int(midi_events[0][0][1]) in [1,2,3,4]) & (int(midi_events[0][0][2]) ==0) & (int(midi_events[0][0][3]) ==0) & (int(midi_events[0][0][0]) ==192): #Light
                        pLight = int(midi_events[0][0][1])-1
                        #print(pLight)
                        newSetting = True
                elif(int(midi_events[0][0][0]) ==176) & (int(midi_events[0][0][1]) ==7) & (int(midi_events[0][0][3]) ==0): #Brightness
                        pBrightness = int(midi_events[0][0][2])
                        if pLight == 3:
                                for l in lights:
                                        l.brightness = pBrightness*2
                        else:
                                lights[pLight].brightness = pBrightness*2
                        newSetting = True
                elif(int(midi_events[0][0][0]) ==224) & (int(midi_events[0][0][1]) ==0) & (int(midi_events[0][0][3]) ==0): #Saturation
                        pSaturation = int(midi_events[0][0][2])
                        if pLight == 3:
                                for l in lights:
                                        l.saturation = pSaturation*2
                        else:
                                lights[pLight].saturation = pSaturation*2
                        newSetting = True
                elif(int(midi_events[0][0][0]) ==176) & (int(midi_events[0][0][1]) ==1) & (int(midi_events[0][0][3]) ==0): #Hue
                        pHue = int(midi_events[0][0][2])
                        if pLight == 3:
                                for l in lights:
                                        l.hue = pHue*516
                        else:
                                lights[pLight].hue = pHue*516
                        newSetting = True
                elif((int(midi_events[0][0][0]) ==144) & (int(midi_events[0][0][1])-37 == 47) & (int(midi_events[0][0][2]) == 0)): #Toggle lights on/off
                        if lights[1].on == True:
                                for l in lights:
                                        l.on = False
                        else:
                                for l in lights:
                                        l.on = True
                elif(int(midi_events[0][0][0]) ==144) & ((int(midi_events[0][0][1])-37) < 47): #KeyboardPresets
                        #print(int(midi_events[0][0][1])-37)
                        lights[0].brightness = saveStruct[int(midi_events[0][0][1])-37][0][0]
                        lights[1].brightness = saveStruct[int(midi_events[0][0][1])-37][1][0]
                        lights[2].brightness = saveStruct[int(midi_events[0][0][1])-37][2][0]
                        lights[0].saturation = saveStruct[int(midi_events[0][0][1])-37][0][2]
                        lights[1].saturation = saveStruct[int(midi_events[0][0][1])-37][1][2]
                        lights[2].saturation = saveStruct[int(midi_events[0][0][1])-37][2][2]
                        lights[0].hue = saveStruct[int(midi_events[0][0][1])-37][0][1]
                        lights[1].hue = saveStruct[int(midi_events[0][0][1])-37][1][1]
                        lights[2].hue = saveStruct[int(midi_events[0][0][1])-37][2][1]


print "exit"
