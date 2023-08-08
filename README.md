# HANDS2023-AssemblyHands

This repository offers a submission guidance for the [ICCV 2023 HANDS challenge - Task 1](https://sites.google.com/view/hands2023/challenges/task1?authuser=0).

You can find test images and files (including image path, bbox).
[test images](https://drive.google.com/drive/folders/1Vsh4V_7JLyycP8c13_RVPpXhmlQaJhdD?usp=sharing)
[test files](https://drive.google.com/drive/folders/1hqqh5ZnbLdDEbXZS_jv4iAVfkQPguLMA?usp=drive_link)

We will evaluate two-hand prediction in world coordinates. 


The frame indices used in test evaluation are listed in `template/assemblyhands_test_joint_3d_iccv23_pred_template.json`. \
Note: we filtered out samples that are not suitable for evaluation (e.g., the hand is partially out of view) from the test set provided in the [toolkit](https://github.com/facebookresearch/assemblyhands-toolkit). Please make sure your results have the entries listed in the template json.


The headset used in the capture has four egocentric cameras. It means 

ensamble?

The script `challenge_submit.py` creates your own prediction file in the json format.
Please custom the `get_pred(.)` function to register in your results.
By default, the script sets your prediction as zero and saves them to `assemblyhands_test_joint_3d_iccv23_pred.json`.

nusar-2021_action_both_9061-c13d_9061_user_id_2021-02-09_143830

