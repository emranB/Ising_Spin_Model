import sys, json
from modules.isingSpinModel import IsingSpingModel
from modules.isingSpinModel_SciPy import IsingSpinModel_SciPy

CONFIG_INPUT_FILE_PATH = './config.json'


if __name__=="__main__":
    # Check if valid config is provided
    cfg = {}
    with open(CONFIG_INPUT_FILE_PATH) as cfgData:
        cfg = json.load(cfgData)
        if not len(cfg):
            print(f'Invalid config file at {CONFIG_INPUT_FILE_PATH}.')
            sys.exit(0)
    print("Valid config file found. Initializing...")
    print("..................................................")

    # Run standalone model
    if cfg['run-standalone-model']:
        with open(cfg['input-file-path']) as fileData:
            print("Running standalone model...")
            ism = IsingSpingModel(fileDataPointer=fileData, debug=cfg['debug'])
            ism_groundStateEnergy = ism.groundStateEnergy()
            if (ism_groundStateEnergy):
                print("Ground state energy = ", ism_groundStateEnergy[0])
                print("Sping configuration = ", ism_groundStateEnergy[1])
            print("....................Done..........................\r\n")

    # Run scipy minimizing model
    if cfg['run-scipy-model']:
        with open(cfg['input-file-path']) as fileData:
            print("Running scipy model...")
            ismsp = IsingSpinModel_SciPy(fileDataPointer=fileData, debug=cfg['debug'])
            ismsp_groundStateEnergy = ismsp.groundStateEnergy()
            if (ismsp_groundStateEnergy):
                print("Ground state energy = ", ismsp_groundStateEnergy[0])
                print("Sping configuration = ", ismsp_groundStateEnergy[1])
            print("....................Done..........................\r\n\r\n")

    # Run tests
    for i, test in enumerate(cfg['tests']):
        if test['skip']: continue

        print(f'TEST {i}: Running standalone model...')
        with open(test['input-file-path']) as fileData:
            ism = IsingSpingModel(fileDataPointer=fileData, debug=cfg['debug'])
            ism_groundStateEnergy = ism.groundStateEnergy()
            if (ism_groundStateEnergy):
                print("Ground state energy = ", ism_groundStateEnergy[0], "Expected: ", test['expected-output'][0])
                print("Sping configuration = ", ism_groundStateEnergy[1], "Expected: ", test['expected-output'][1])

        print("..................................................")

        print(f'TEST {i}: Running scipy model...')
        with open(test['input-file-path']) as fileData:
            ism = IsingSpingModel(fileDataPointer=fileData, debug=cfg['debug'])
            ism_groundStateEnergy = ism.groundStateEnergy()
            if (ism_groundStateEnergy):
                print("Ground state energy = ", ism_groundStateEnergy[0], "Expected: ", test['expected-output'][0])
                print("Sping configuration = ", ism_groundStateEnergy[1], "Expected: ", test['expected-output'][1])
            
        print("....................Done..........................\r\n\r\n")

    print("Exiting...")



