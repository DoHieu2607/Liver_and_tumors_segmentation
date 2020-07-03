# Liver_and_tumors_segmentation

Đây là bài nghiên cứu khoa học cấp sinh viên trường Đại học Sài Gòn. Tên đề tài: Áp dụng tính toán thông minh để trích xuất gan và u gan trên ảnh MR 3D. Mục tiêu của đề tài này là đề xuất mô hình sử dụng các thuật toán để trích xuất gan và u gan trên ảnh MR. Nhóm nghiên cứu đã đề xuất mô hình sử dụng thuật toán FCN trong deep learning với kiến trúc Unet 2D để giải quyết bài toán này. 

## Data

Bộ dữ liệu nhóm nghiên cứu sử dụng được đề cập trong bài báo của tác giả [Hieu Trung Huynh](https://link.springer.com/article/10.1007/s11548-016-1498-9) (vì tính bảo mật của dữ liệu, nhóm nghiên cứu sẽ không public data).

## Getting Started
 Để phục vụ cho ra kết quả trong nghiên cứu này, nhóm nghiên cứu đã sử dụng ggColab để chạy mô hình trích xuất gan, u gan. Toàn bộ thông tin xử lý dữ liệu và xây dựng mô hình được miêu tả trong file tóm tắt [liver_segmentation](https://github.com/hieukut456/Liver_and_tumors_segmentation/blob/master/liver_segmentation.docx). 

Toàn bộ code chương trình, bao gồm:
 + Trích xuất gan nằm trong file [liver_segmentationn.ipynb](https://github.com/hieukut456/Liver_and_tumors_segmentation/blob/master/Liver_segmentation.ipynb).
 + Trích xuất u gan nằm trong file [liver_tumor_segmentation.ipynb](https://github.com/hieukut456/Liver_and_tumors_segmentation/blob/master/Liver_tumor_segmentation)

## Results

Toàn bộ kết quả sẽ được hiển thị trong file results.ipynb.
