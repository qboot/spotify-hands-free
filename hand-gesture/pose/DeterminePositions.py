from pose.utils.FingerCurled import FingerCurled
from pose.utils.FingerPosition import FingerPosition
from pose.utils.FingerDataFormation import FingerDataFormation

def determine_position(curled_positions, finger_positions, known_finger_poses, min_threshold):
    obtained_positions = {}

    for finger_pose in known_finger_poses:
        score_at = 0.0
        for known_curl, known_curl_confidence, given_curl in \
            zip(finger_pose.curl_position, finger_pose.curl_position_confidence, curled_positions):
                if len(known_curl) == 0:
                    if len(known_curl_confidence) == 1:
                        score_at += known_curl_confidence[0]
                        continue

                if given_curl in known_curl:
                    confidence_at = known_curl.index(given_curl)
                    score_at += known_curl_confidence[confidence_at]

        for known_position, known_position_confidence, given_position in \
            zip(finger_pose.finger_position, finger_pose.finger_position_confidence, finger_positions):
                if len(known_position) == 0:
                    if len(known_position_confidence) == 1:
                        score_at += known_position_confidence[0]
                        continue

                if given_position in known_position:
                    confidence_at = known_position.index(given_position)
                    score_at += known_position_confidence[confidence_at]

        if score_at >= min_threshold:
            obtained_positions[finger_pose.position_name] = score_at

    return obtained_positions

def get_position_name_with_pose_id(pose_id, finger_poses):
    for finger_pose in finger_poses:
        if finger_pose.position_id == pose_id:
            return finger_pose.position_name
    return None


def create_known_finger_poses():
    known_finger_poses = []

    ####### 1 Thumbs up
    thumbs_up = FingerDataFormation()
    thumbs_up.position_name = 'Play'
    thumbs_up.curl_position = [
        [FingerCurled.NoCurl],   # Thumb
        [FingerCurled.FullCurl], # Index
        [FingerCurled.FullCurl], # Middle
        [FingerCurled.FullCurl], # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    thumbs_up.curl_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    thumbs_up.finger_position = [
        [FingerPosition.VerticalUp], # Thumb
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight], # Index
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight], # Middle
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight], # Ring
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight] # Little
    ]
    thumbs_up.finger_position_confidence = [
        [1.0], # Thumb
        [1.0, 1.0], # Index
        [1.0, 1.0], # Middle
        [1.0, 1.0], # Ring
        [1.0, 1.0]  # Little
    ]
    thumbs_up.position_id = 0
    known_finger_poses.append(thumbs_up)

    ####### 2 Pause o
    pause = FingerDataFormation()
    pause.position_name = 'Pause'
    pause.curl_position = [
        [FingerCurled.NoCurl],   # Thumb
        [FingerCurled.HalfCurl], # Index
        [FingerCurled.HalfCurl], # Middle
        [FingerCurled.HalfCurl], # Ring
        [FingerCurled.HalfCurl]  # Little
    ]
    pause.curl_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    pause.finger_position = [
        [FingerPosition.DiagonalUpLeft], # Thumb
        [FingerPosition.DiagonalUpLeft], # Index
        [FingerPosition.DiagonalUpLeft], # Middle
        [FingerPosition.DiagonalUpLeft], # Ring
        [FingerPosition.DiagonalUpLeft] # Little
    ]
    pause.finger_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    pause.position_id = 2
    known_finger_poses.append(pause)

    ####### 3 Volume Up
    volume_up = FingerDataFormation()
    volume_up.position_name = 'Volume Up'
    volume_up.curl_position = [
        [FingerCurled.NoCurl],   # Thumb
        [FingerCurled.NoCurl], # Index
        [FingerCurled.NoCurl], # Middle
        [FingerCurled.NoCurl], # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    volume_up.curl_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    volume_up.finger_position = [
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpLeft], # Thumb
        [FingerPosition.VerticalUp], # Index
        [FingerPosition.VerticalUp], # Middle
        [FingerPosition.VerticalUp], # Ring
        [FingerPosition.VerticalUp] # Little
    ]
    volume_up.finger_position_confidence = [
        [1.0, 0.5], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    volume_up.position_id = 2
    known_finger_poses.append(volume_up)

    ####### 4 Volume Down
    volume_down = FingerDataFormation()
    volume_down.position_name = 'Volume Down'
    volume_down.curl_position = [
        [FingerCurled.NoCurl],   # Thumb
        [FingerCurled.NoCurl], # Index
        [FingerCurled.NoCurl], # Middle
        [FingerCurled.NoCurl], # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    volume_down.curl_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    volume_down.finger_position = [
        [FingerPosition.VerticalDown], # Thumb
        [FingerPosition.VerticalDown], # Index
        [FingerPosition.VerticalDown], # Middle
        [FingerPosition.VerticalDown], # Ring
        [FingerPosition.VerticalDown] # Little
    ]
    volume_down.finger_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    volume_down.position_id = 3
    known_finger_poses.append(volume_down)

    ####### 5 Hand left
    hand_left = FingerDataFormation()
    hand_left.position_name = 'Previous Track'
    hand_left.curl_position = [
        [FingerCurled.NoCurl],   # Thumb
        [FingerCurled.NoCurl], # Index
        [FingerCurled.NoCurl], # Middle
        [FingerCurled.NoCurl], # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    hand_left.curl_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    hand_left.finger_position = [
        [FingerPosition.HorizontalRight], # Thumb
        [FingerPosition.HorizontalRight], # Index
        [FingerPosition.HorizontalRight], # Middle
        [FingerPosition.HorizontalRight], # Ring
        [FingerPosition.HorizontalRight] # Little
    ]
    hand_left.finger_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    hand_left.position_id = 4
    known_finger_poses.append(hand_left)

    ####### 6 Hand right
    hand_right = FingerDataFormation()
    hand_right.position_name = 'Next Track'
    hand_right.curl_position = [
        [FingerCurled.NoCurl],   # Thumb
        [FingerCurled.NoCurl], # Index
        [FingerCurled.NoCurl], # Middle
        [FingerCurled.NoCurl], # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    hand_right.curl_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    hand_right.finger_position = [
        [FingerPosition.HorizontalLeft], # Thumb
        [FingerPosition.HorizontalLeft], # Index
        [FingerPosition.HorizontalLeft], # Middle
        [FingerPosition.HorizontalLeft], # Ring
        [FingerPosition.HorizontalLeft] # Little
    ]
    hand_right.finger_position_confidence = [
        [1.0], # Thumb
        [1.0], # Index
        [1.0], # Middle
        [1.0], # Ring
        [1.0]  # Little
    ]
    hand_right.position_id = 5
    known_finger_poses.append(hand_right)

    return known_finger_poses
