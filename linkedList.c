#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node* next;
};

struct node* head = NULL;

void
getLength(void) {
	struct node* current = head;
	size_t len = 0;

	while (current) {
		current = current->next;
		len++;
	}

	printf("Length = %d\n", len);

}

void 
insertAtFront(int data) {
	struct node* new_node = (struct node*)malloc(sizeof(struct node));
	new_node->data = data;
	new_node->next = head;

	head = new_node;
}


void 
insertAtEnd(int data) {
	
	do {

		struct node* new_node = (struct node*)malloc(sizeof(struct node));
		new_node->data = data;
		new_node->next = NULL;

		// if empty list
		if (!head) {
			head = new_node;
		}
		else {
			struct node* current = head;

			while (current->next) {
				current = current->next;
			}

			current->next = new_node;
		}

	} while (0);
	
}

void 
printList(void) {
	struct node* current = head;

	while (current) {
		printf(" %d ", current->data);
		current = current->next;
	}
	printf("\n");
}

void 
removeNode(int data) {
	struct node* current = head;

	do {

		// if head node is one to be deleted
		if (head->data == data) {
			head = head->next;
			break;
		}

		struct node* prev = (struct node*)malloc(sizeof(struct node));
    
		while (current->next) {

      // if node to be deleted was found
			if (current->data == data) {
				break;
			}

			prev = current;
			current = current->next;
		}

    // if node to be deleted was not found
		if (current->data != data) {
			printf("Could not find node %d\n", data);
			break;
		}

    // remove node
		prev->next = current->next;
		

	} while (0);
}


int main() {
	
	insertAtEnd(5);
	insertAtEnd(6);
	insertAtEnd(7);

	insertAtFront(8);

	removeNode(6);
	
	printList();
	getLength();
		

	
	
	return 0;
	

}
