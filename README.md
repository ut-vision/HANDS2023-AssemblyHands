# HANDS2023-AssemblyHands
This repository offers a submission guidance for the [ICCV 2023 HANDS challenge - AssemblyHands](https://sites.google.com/view/hands2023/challenges/assemblyhands).
The task is 3D hand pose estimation from an egocentric view.

## Release notes
\[Aug 26, 202\]: Add the instructions for "How to lift to world coordinates" \
\[Aug 26, 202\]: Update test files (v1-3).  Please check the total stats (n_img: 61725, n_kpt: 25885) and ``test_seq_stats `` in `chllenge_submit.py`.

## Test image and metadata
You can find test images and files (including image path, bbox): \
[[test images]](https://drive.google.com/drive/folders/1Vsh4V_7JLyycP8c13_RVPpXhmlQaJhdD?usp=sharing) 
[[test files]](https://drive.google.com/drive/folders/18p4kF6BmArKGp3cac7Ww4TjfYcbHbYRs?usp=drive_link) \
Please place the `template/` folder under this directory. \
Note: the image size of `nusar-2021_action_both_9061-c13d_9061_user_id_2021-02-09_143830` is realatively smaller than others due to a headset malfunction that stopped the image export midway.

## Evaluation details
We will evaluate two-hand predictions in world coordinates. The format should be consistent with that of the 3D keypoint annotation.

The data file `assemblyhands_test_ego_data_iccv23-${version}.json` defines the input images that can be used for test dataloader.
The final submission format is specified by `template/assemblyhands_test_joint_3d_iccv23-${version}_pred_template.json`. \
Note: we've filtered out images that are not suitable for evaluation (e.g., the hand is partially out-of-view). 
This results in less frame indices than those in the test image folder.

Before submission, please make sure the following notes:
- Two-hand format (42 keypoints are defined for each frame)
- Frame indices match the template json
- Leave the prediction blank (fill in 0s) if the hand bbox is not provided in the data file

## How to lift to world coordinates and visualization
Please use ``assemblyhands_test_abs_depth_iccv23-${version}.json`` to get [abs_depth](https://github.com/facebookresearch/assemblyhands-toolkit/blob/ad20e4a37ec0bcde1f4e13338f6c25ef5ce25712/src/dataset/AssemblyHands-Ego/dataset.py#L153C15-L153C15) for the test images.
This allows to convert the prediction in camera coordinates to world coordinates.

To provide a two-hand pose format, you may need to combine single-view predictions in post-processing.
Since the headset has multiple cameras, you may have muliple predictions in the same scene.
You can postprocess to merge them by ensemble or some fusion techniques.
The image file name (e.g., "000554.jpg") is defined identically across multi-cameras (id: HMC*).
The multi-view images have the same frame name but with different camera names.

In addtion, you can test the generated two-hand format by the [visualizer](https://github.com/facebookresearch/assemblyhands-toolkit#visualization) in the toolkit.

## Submission instructions
The script `challenge_submit.py` will create your own json file using the template file.
Please custom the `get_pred(.)` function to register in your results.
By default, the function fills in zeros and saves them to `assemblyhands_test_joint_3d_iccv23_pred.json`.
Finally, please upload your prediction file as a zip file to the evaluation server.

## References
- [AssemblyHands Toolkit](https://github.com/facebookresearch/assemblyhands-toolkit)
- [ICCV 2023 HANDS Workshop](https://sites.google.com/view/hands2023/home)

## Acknowledgment
We thank Dr. Linlin Yang, Prof. Angela Yao (NUS), Dr. Kun He (Meta), and Prof. Yoichi Sato (UTokyo) for helpful discussions on the design of the challenge. This dataset is based on the internship work at Meta Reality Labs, and thanks go to Dr. Fadime Sener, Dr. Tomas Hodan, Dr. Luan Tran, and Dr. Cem Keskin (Meta). We also thank Mr. Nie Lin (UTokyo) for the baseline construction. 