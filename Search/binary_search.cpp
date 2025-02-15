int binary_serch(vector<int> list, int target){
    int low = 0;
    int high = list.size() - 1;
    int min;
    
    while( low <= high ){
        mid = low + (high - low)/2;
        
        if( list[mid] == target) return mid;
        if( list[mid] < target ){
            high = mid;
        }    
        if( list[mid] > target ){
            low = mid;
        }
    }
    return -1;
}

int binary_search_recursize(vector<int> list, int low, int high, int target){
    if(high >= low){
        int mid = low + (high - low)/2;
        if(list[mid] == target) return mid;
        if(list[mid] < target) return binary_search_recursive(list,low,mid-1,target);
        if(list[mid] > target) return binary_search_recursize(list,mid+1,high,target);
    }
    return -1;
}