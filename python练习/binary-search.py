# coding=utf-8

def binary_search(list,target):
    if not list:
        return -1 # -1表示找不到目标值
    else:
        left=0
        right=len(list)-1
        while left<=right:
            mid=int((left+right)/2)  # 使用int()方法，保证mid为整数
            if list[mid]==target:
                return mid
            elif list[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1  # -1表示找不到目标值


if __name__=="__main__":
    list1=[1,2,4,5,6,23,33,45]
    target_index=binary_search(list1,25)
    print(target_index)