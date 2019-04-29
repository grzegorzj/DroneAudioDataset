# DroneAudioDataset

This repo consists of drone audio dataset which has been recorded of drone propellers noise in an indoor environment by Sara Al-Emadi and artificially augmented with random noise clips. The drone audio dataset is part of 'Audio Based Drone Detection and Identification using Deep Learning' conference paper which can be found in _________ . 

The noise clips that categorised as 'Unknown' in both binary and multiclass folders are used from the open-source project ESC: Dataset for Environmental Sound Classification by Karol J. Piczak (https://github.com/karoldvl/ESC-50) and the white noise from Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition by Pete Warden (https://arxiv.org/pdf/1804.03209.pdf and https://www.tensorflow.org/tutorials/sequences/audio_recognition). In addition, we have created our own silence audio clip to balance the dataset.

## Attribution ##

If you use this dataset in your research, cite via the following BibTeX:

@INPROCEEDINGS{AlEm1906:Audio,
AUTHOR=”Sara A Al-Emadi and Abdulla K Al-Ali and Abdulaziz Al-Ali and Amr Mohamed”,
TITLE=”Audio Based Drone Detection and Identification using Deep Learning”,
BOOKTITLE=”IWCMC 2019 Vehicular Symposium (IWCMC-VehicularCom 2019)”,
ADDRESS=”Tangier, Morocco”,
DAYS=23,
MONTH=jun,
YEAR=2019,
}

