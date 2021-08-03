def count_smileys(arr):
    s = [":)",":D",":-)",";-)",";)",";D",";-D",":~)",";~D",";)",":-D",":~D"]
    count = 0
    for smile in arr:
        if smile in s:
            count += 1
    return count