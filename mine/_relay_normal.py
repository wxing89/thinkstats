import relay
import rankit

def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    rankit.MakeNormalPlot(speeds,
                          root='relay_normal',
                          ylabel='Speed (MPH)')


if __name__ == '__main__':
    main()

