import numpy as np
import json

# NOTE: the number of samples in each test sequence.
# Please check the number before your submition.
test_seq_stats = {
    "nusar-2021_action_both_9034-c08b_9034_user_id_2021-02-04_161726": 8332,
    "nusar-2021_action_both_9021-c10a_9021_user_id_2021-02-23_100458": 7501,
    "nusar-2021_action_both_9061-c13d_9061_user_id_2021-02-09_143830": 3192,
    "nusar-2021_action_both_9074-a29_9074_user_id_2021-02-11_154856": 6923,
}

def get_pred(img=None, camera_intrinsic=None, camera_extrinsic=None):
    """ 
    Custom your algorithm to get 3D joint coordinates from a given sample.
    input: custom by yourself
    output: 3D pose of two hands in world coordinates (42, 3)
    """
    xyz = np.zeros((42, 3))
    return xyz

with open('template/assemblyhands_test_joint_3d_iccv23_pred_template.json', 'r') as f:
    kpt_pred = json.load(f) # fill in -1 by default

total_samples = 0
for seq_name in test_seq_stats.keys():
    frame_id_list = kpt_pred['annotations'][seq_name].keys()
    for frame_id in frame_id_list:        
        pts_3d_pred = get_pred() # get your prediction        
        kpt_pred['annotations'][seq_name][frame_id]['world_coord'] = pts_3d_pred.tolist() # update the item in kpt_pred
        total_samples += 1

# n_samples check
assert total_samples == sum(test_seq_stats.values()), "The total number of samples is not correct: {} vs {}".format(total_samples, sum(test_seq_stats.values()))

output_path = 'assemblyhands_test_joint_3d_iccv23_pred.json'
with open(output_path, 'w') as f:
    json.dump(kpt_pred, f)
print('Dumped %d joints to %s' % (total_samples, output_path))