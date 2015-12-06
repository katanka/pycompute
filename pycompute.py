from utils.Constant import Constant

def main():
	constant = Constant.getInstanceFromString('x	5	m^2*s^-4/y*s')
	print constant.units

if __name__ == "__main__": main()