from navigation.direction import Direction
import vision_agent as va
import game_window_grid as gwg
import auto_trainer.controllers.window_controller as wc


class Localizer:
    _old_region_img = None

    @staticmethod
    def prepare_for_move(direct):
        if direct == Direction.up:
            old_region = gwg.get_row_range_rect(1, gwg.num_rows() - 2)
        elif direct == Direction.down:
            old_region = gwg.get_row_range_rect(2, gwg.num_rows() - 1)
        elif direct == Direction.left:
            old_region = gwg.get_col_range_rect(0, gwg.num_cols() - 1)
        elif direct == Direction.right:
            old_region = gwg.get_col_range_rect(1, gwg.num_cols())
            print('Old region:', old_region)
        else:
            raise ValueError('Invalid direction')
        Localizer._old_region_img = va.screenshot(
            # 'img/ss_test/localizer/old_img.png',
            region=old_region)

    @staticmethod
    def has_moved_in_direction(direct, confidence=0.8):
        if direct == Direction.up:
            new_region = gwg.get_row_range_rect(2, gwg.num_rows() - 1)
        elif direct == Direction.down:
            new_region = gwg.get_row_range_rect(1, gwg.num_rows() - 2)
        elif direct == Direction.left:
            new_region = gwg.get_col_range_rect(1, gwg.num_cols())
        elif direct == Direction.right:
            new_region = gwg.get_col_range_rect(0, gwg.num_cols() - 1)
            print('New region:', new_region)
        else:
            raise ValueError('Invalid direction: ' + direct)
        #va.screenshot('img/ss_test/localizer/new_img.png', region=new_region)
        return va.is_in_region(Localizer._old_region_img,
                               region=new_region, confidence=confidence)
