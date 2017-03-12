#include<stdio.h>
#include<stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* insert(struct ListNode *root, int *arr, int len){
    struct ListNode *org = root; 
    for(int i=0; i<len; i++){
        //printf(" %d: %d", i, *(arr+i));
        struct ListNode *p = (struct ListNode*)malloc(sizeof(struct ListNode));
        p->val = *(arr+i);
        p->next = NULL;
        root->next = p;
        root = root->next;
    }
    return org;
}

void traverse(struct ListNode *node){
    if(node){
        printf(" %d ", node->val);
        traverse(node->next);
    }
}
struct ListNode* merge(struct ListNode* left, struct ListNode *right){

    struct ListNode n = {0};
    struct ListNode *p = &n;
    while(left && right){
        if(left->val < right->val){
            p = p->next = left;
            left = left->next;
        }
        else{
            p = p->next = right;
            right = right->next;
        }
//        printf(" p->next: %d", p->next->val);
    }
    p->next = left? left: right;
    return n.next;
}

struct ListNode* sortedList(struct ListNode *head){

    int i = 0;
    if(head == NULL || head->next == NULL){
        return head;
    }
    struct ListNode *faster = head, *slower = head, *prev, *left, *right;
    while(faster && faster->next){
        prev = slower;
        faster = faster->next->next;
        slower = slower->next;
    }
    prev->next = NULL;
    return merge(sortedList(head), sortedList(slower));
}



int main(){
    struct ListNode *root =  (struct ListNode*)malloc(sizeof(struct ListNode));
    root->val = 0;
    int arr[15] = {14, 3, 5, 8, 20, 6, 99, 2, 7, 9, 13, 19, 1, 31, 5};
    int len = sizeof(arr);
    root = insert(root, arr, 15);
    traverse(root);
    root = sortedList(root);
    printf("\n");
    traverse(root);
}

