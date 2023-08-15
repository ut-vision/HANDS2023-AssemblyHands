# HANDS2023-AssemblyHands

This repository offers a submission guidance for the [ICCV 2023 HANDS challenge - AssemblyHands](https://sites.google.com/view/hands2023/challenges/assemblyhands).
The task is 3D hand pose estimation from an egocentric view.

## Test image and metadata
You can find test images and files (including image path, bbox): \
[[test images]](https://drive.google.com/drive/folders/1Vsh4V_7JLyycP8c13_RVPpXhmlQaJhdD?usp=sharing) \
[[test files]](https://drive.google.com/drive/folders/1hqqh5ZnbLdDEbXZS_jv4iAVfkQPguLMA?usp=drive_link) \
Please place the `template/` folder under this directory. \
Note: the image size of `nusar-2021_action_both_9061-c13d_9061_user_id_2021-02-09_143830` is realatively smaller than others due to a headset malfunction that stopped the image export midway.

## Evaluation details
We will evaluate two-hand predictions in world coordinates. The format should be consistent with that of the 3D keypoint annotation.

The data file `assemblyhands_test_ego_data_iccv23.json` defines the input images that can be used for test dataloader.
The final submission format is specified by `template/assemblyhands_test_joint_3d_iccv23_pred_template.json`. \
Note: we've filtered out images that are not suitable for evaluation (e.g., the hand is partially out-of-view). 
The frame indices in the template file are less than those in the test image folder.

Before submission, please make sure the following notes:
- Two-hand format (42 keypoints are defined for each frame)
- Frame indices match the template json
- Leave the prediction blank (fill in 0s) if the hand bbox is not provided in the data file

Since the headset has multiple cameras, you may have muliple predictions in the same scene.
You can postprocess to merge them (e.g., ensemble) and provide a two-hand pose format every frame.
The image file name (e.g., "000554.jpg") is defined identically across multi-cameras (id: HMC*).
You can find multi-view images with the same frame name but with different camera names.

In addtion, you can test the generated two-hand format by the [visualizer](https://github.com/facebookresearch/assemblyhands-toolkit#visualization) in the toolkit.

## Submission instruction
The script `challenge_submit.py` will create your own json file using the template file.
Please custom the `get_pred(.)` function to register in your results.
By default, the function fills in zeros and saves them to `assemblyhands_test_joint_3d_iccv23_pred.json`.
Finally, please upload your prediction file to the evaluation server (TBD).

## References
- [AssemblyHands Toolkit](https://github.com/facebookresearch/assemblyhands-toolkit)
- [ICCV 2023 HANDS Workshop](https://sites.google.com/view/hands2023/home)

## Acknowledgment
We thank Dr. Linlin Yang, Prof. Angela Yao (NUS), Dr. Kun He (Meta), and Prof. Yoichi Sato (UTokyo) for helpful discussions on the design of the challenge. This dataset is based on the internship work at Meta Reality Labs, and thanks go to Dr. Fadime Sener, Dr. Tomas Hodan, Dr. Luan Tran, and Dr. Cem Keskin (Meta). We also thank Mr. Nie Lin (UTokyo) for the baseline construction. 