from navigation.direction import Direction
import vision_agent as va
import window_grid as grid
import window_controller as wc


class Localizer:
    _old_region_img = None

    @staticmethod
    def prepare_for_move(direct):
        if direct == Direction.up:
            old_region = grid.get_row_range_rect(1, grid.num_rows() - 2)
        elif direct == Direction.down:
            old_region = grid.get_row_range_rect(2, grid.num_rows() - 1)
        elif direct == Direction.left:
            old_region = grid.get_col_range_rect(0, grid.num_cols() - 1)
        elif direct == Direction.right:
            old_region = grid.get_col_range_rect(1, grid.num_cols())
        else:
            raise ValueError('Invalid direction')
        Localizer._old_region_img = va.screenshot(
            'img/localizer/old_img.png', region=old_region)

    @staticmethod
    def has_moved_in_direction(direct, confidence=0.8):
        if direct == Direction.up:
            new_region = grid.get_row_range_rect(2, grid.num_rows() - 1)
        elif direct == Direction.down:
            new_region = grid.get_row_range_rect(1, grid.num_rows() - 2)
        elif direct == Direction.left:
            new_region = grid.get_col_range_rect(1, grid.num_cols())
        elif direct == Direction.right:
            new_region = grid.get_col_range_rect(0, grid.num_cols() - 1)
        else:
            raise ValueError('Invalid direction: ' + direct)
        va.screenshot('img/localizer/new_img.png', region=new_region)
        return va.is_in_region(Localizer._old_region_img, region=new_region, confidence=confidence)