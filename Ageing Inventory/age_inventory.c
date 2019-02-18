//
//  age_inventory.c
//  
//
//  Created by Abhijeet Singh on 19/11/18.
//
//

#include <stdio.h>
send_item(int *left,int k) {
    int l[10];
    int i,j,m;
    //bubble sort left[]+t[][k] create an array with ascending order for l[]
    i = 0;
    while(left[k]!=0 && k != l[i]) {
        if(left[k]>left[[i+1]]-left[l[i]]) {
            left[k] -= left[[i+1]]-left[l[i]];
            m = left[[i+1]]-left[l[i]]/(i+1);
            for(j=0;j<=i;++j) {
                left[l[j]] += k;
                }
        }
        else if(left[k]<left[[i+1]]-left[k]){
            m = left[k]/(i+1);
            left[k] = 0;
            for(j=0;j<=i;++j) {
                left[l[j]] += m;
            }
        }
        ++i;
    }
}
receive_item(int *left,int k) {
    int l[10];
    int i,j,m;
    //bubble sort left[]+t[][k] create an array with ascending order for l[]
    i = 9;
    while(k != l[i]) {
        if(left[k]>left[[i+1]]-left[l[i]]) {
            left[k] -= left[[i+1]]-left[l[i]];
            m = left[[i+1]]-left[l[i]]/(i+1);
            for(j=0;j<=i;++j) {
                left[l[j]] += k;
            }
        }
        ++i;
    }
}
main() {
    int left[10];
    int age[10];
    int t[10][10];
    int i;
    for(i=0;i<10;++i) {
        if(age[i] == 0 && left[i]>0)
        send_item(left,i);
        if(left[i] <= 0)
        receive_item(left,i);
    }
    
}
