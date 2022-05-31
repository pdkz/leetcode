class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2[0], rec2[1], rec2[2], rec2[3]

        rec1_w, rec1_h = rec1_x2 - rec1_x1, rec1_y2 - rec1_y1
        rec2_w, rec2_h = rec2_x2 - rec2_x1, rec2_y2 - rec2_y1

        rec1_cx, rec1_cy = rec1_x1 + rec1_w // 2, rec1_y1 + rec1_h // 2
        rec2_cx, rec2_cy = rec2_x1 + rec2_w // 2, rec2_y1 + rec2_h // 2

        if (abs(rec1_cx - rec2_cx) < rec1_w // 2 + rec2_w // 2) and \
        (abs(rec1_cy - rec2_cy) < rec1_h // 2 + rec2_h // 2):
            return True

        return False
