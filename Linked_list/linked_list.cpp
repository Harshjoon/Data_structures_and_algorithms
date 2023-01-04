#include <iostream>
using namespace std;

class Node{
    public:
        int data;
        Node* next;
        // Default Constructor
        Node(){
            data = 0;
            next = NULL;
        }
        // Constructor
        Node(int data){
            this->data = data;
            this->next = NULL;
        }
};

class LinkedList{
    Node* head;
    public:
        // Default constructor
        LinkedList(){head=NULL};
        // Class member functions
        void insertNode(int);
        void print();
        void deleteNode(int);
};

void LinkedList::insertNode(int data){
    Node* newNode = new Node(data);
    if(head==NULL){
        head = newNode;
        return;
    }
    Node* temp = head;
    while(temp->next){
        temp = temp->next;
    }
    temp->next = newNode;
    return;
}
void LinkedList::print(){
    Node* temp = head;
    if (head==NULL){
        cout << "" << endl;
    }
    while(temp!=NULL){
        cout << temp->data << "->";
        temp = temp->next;
    }
}
void LinkedList::deleteNode(int nodeOffset){
    Node*temp1 = head, *temp2=NULL;
    if(head==NULL){
        cout << "Empty List." << endl;
        return;
    }
    int len = 0;
    while(temp1 != NULL){
        temp1 = temp1->next;
        len++;
    }
    if(len<nodeOffset){
        cout << "index out of range." << endl;
    }
    if(nodeOffset==1){
        head = head->next;
        delete temp1;
        return;
    }
    while(nodeOffset-->1){
        temp2 = temp1;
        temp1 = temp1->next;
    }
    temp2->next = temp1->next;
    delete temp1;
}

int main(){
    LinkedList list;
    // insert nodes
    list.insertNode(1);
    list.insertNode(2);
    list.insertNode(3);

    list.print();
}















