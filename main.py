import math
def doppler(vx, vy, oy, v, x, period, wSpeed,duration,timeC):
    #timeC is basically frames/second (of simulated time)
    #we want to simulate a source creating pulses at some period and then when it hits the observer, it records one, and we take this to measure frequency
    obs = {
        'vx' : vx, 
        'vy': vy,
        'x': 0,
        'y': oy * timeC #converting to a different unit that is 1/timeC of the inputted unit. Furthermore, out velocities will become different units/frame, so we dont need to scale them.
    }
    src = {
        'v':v,
        'x':x  * timeC
    }
    times = []
    bubbles = []
    frame = 0 
    frame_period = period * timeC
    for i in range(duration * timeC):
        if frame % frame_period == 0 or (frame - frame_period/50) % frame_period == 0 :
            bubbles.append({
                'd': 0,
                'x': src['x'],
            })
        #update bubbles
        obs['x'] += obs['vx']
        obs['y'] += obs['vy']
        src['x'] += src['v']
        i2 = 0
        while i2 < len(bubbles):
            bubble = bubbles[i2]
            bubble['d'] += wSpeed
            dist = math.sqrt((bubble['x'] - obs['x'])**2 + (obs['y'])**2)
            if bubble['d'] >= dist:
                bubbles.pop(i2)
                times.append(frame/timeC)
            else:
                i2 +=1
        frame += 1
    return times

def processtimes(times):
    for i in range(len(times)):
        if i % 2 == 0 and i < len(times) - 1:
            print(1/(times[i+1] - times[i])/50)
    print('seperator')
    for i in range(len(times)):
        if i % 2 == 0 and i < len(times) - 1:
            print((times[i+1] + times[i])/2)
#for standard doppler, -50 = vo, 100 = vs, dx = 1000, To =1, vw = 350
def case1():
    times = doppler(50,0,0,-100,1000,1,350,30, 10000)
    processtimes(times)
#for case 3 doppler, -50 = vxo, 100 = vx, dx = 1000, To =1, vw = 350, dy = 100, duration = 30
def case3():
    times = doppler(50,0,100,-100,1000,1,350,30, 10000)
    processtimes(times)
#for case 4, -100  =vox, 10 = voy, dx = 2000, To = 1, vw = 350, dy = 0, vx = 150, duration = 30
def case4():
    times = doppler(100,10,100,-150,2000,1,350,30,10000)
    processtimes(times)
    #goal of this: I want big numbers BIG. I want no crossover. Mening . .. they must head towards each other, vy must be big
    # vox = -100, voy = 25, dx = 17000m To = 0.5, vw = 350, dy = 500, vx = 50, duration = 30
def casefour():
    times = doppler(100,25,-500,-50,17000,0.5,350,100,100000)
    processtimes(times)
    # vox = 100, voy = -20, dx = 5  To = 1, vw = 350, dy = 500, vx = -50, duration = 100, 
def case4tsu():
    times = doppler(-100,-20,500,50,5,1,350,30,100000)
    processtimes(times)
case4()
# doppler(vx, vy, oy, v, x, period, wSpeed,duration,timeC):
