#animated thread pendulum
import simulation
import plotting

def main():
    result = simulation.run()
    plotting.animate_pendulum(result)

if __name__ == "__main__":
    main()

