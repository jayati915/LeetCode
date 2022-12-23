int maxSubArray(int* nums, int numsSize){
    int sum = 0;
    int maxSum = INT_MIN;

    for (int i = 0; i < numsSize; i++){
        
        sum = sum + nums[i];
        if (sum < nums[i]){
            sum = nums[i];
        }
        if (sum > maxSum){
            maxSum = sum;
        }
        
    }
    
    return maxSum;
}
