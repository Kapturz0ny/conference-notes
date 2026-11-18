import sys
from pathlib import Path
import cv2
import numpy as np

def to_px(y_norm: float, x_norm: float, w: int, h: int) -> list[float]:
    return [x_norm / 1000.0 * w, y_norm / 1000.0 * h]

def main():
    if len(sys.argv) not in (6, 10):
        print("Użycie:")
        print("  Image crop: python process_image.py <file> <ymin> <xmin> <ymax> <xmax>")
        print("  Fixing perspective: python process_image.py <file> <tl_y> <tl_x> <tr_y> <tr_x> <br_y> <br_x> <bl_y> <bl_x>")
        sys.exit(1)

    img_path = Path(sys.argv[1])
    img = cv2.imread(str(img_path))
    if img is None:
        sys.exit(1)

    h, w = img.shape[:2]
    coords = list(map(float, sys.argv[2:]))

    if len(coords) == 4:
        ymin, xmin, ymax, xmax = coords
        x1, y1 = max(0, int(xmin / 1000 * w)), max(0, int(ymin / 1000 * h))
        x2, y2 = min(w, int(xmax / 1000 * w)), min(h, int(ymax / 1000 * h))
        result = img[y1:y2, x1:x2]
    else:
        tl = to_px(coords[0], coords[1], w, h)
        tr = to_px(coords[2], coords[3], w, h)
        br = to_px(coords[4], coords[5], w, h)
        bl = to_px(coords[6], coords[7], w, h)

        src = np.array([tl, tr, br, bl], dtype="float32")
        max_w = int(max(np.linalg.norm(src[2] - src[3]), np.linalg.norm(src[1] - src[0])))
        max_h = int(max(np.linalg.norm(src[1] - src[2]), np.linalg.norm(src[0] - src[3])))

        dst = np.array([[0, 0], [max_w - 1, 0], [max_w - 1, max_h - 1], [0, max_h - 1]], dtype="float32")
        M = cv2.getPerspectiveTransform(src, dst)
        result = cv2.warpPerspective(img, M, (max_w, max_h), borderMode=cv2.BORDER_REPLICATE)

    out_dir = img_path.parent / "cropped"
    out_dir.mkdir(exist_ok=True)
    cv2.imwrite(str(out_dir / img_path.name), result, [cv2.IMWRITE_JPEG_QUALITY, 92])

if __name__ == "__main__":
    main()