#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node* next;
};

struct node* head = NULL;


void insert_at_end(int data) {
	// create a link
	struct node* new_node = malloc(sizeof(struct node));

	new_node->data = data;
	new_node->next = NULL;

	struct node* current = head;
	do {
		if (!head) {
			head = new_node;
			break;
		}


		while (current->next != NULL) {
			current = current->next;
		}

		current->next = new_node;

	} while (0);
	

	
}

void insert_at_front(int data) {
	// create a link
	struct node* new_node = malloc(sizeof(struct node));

	// set properties for new_node
	new_node->data = data;
	new_node->next = NULL;

	// point to old head node
	new_node->next = head;

	// assign new head node
	head = new_node;
}

void display() {
	struct node* current = head;

	// start from beginning
	while (current) {
		printf("Data : %d  ", current->data);
		current = current->next;
	}
	printf("\n");
}

void remove_node(int data) {
	struct node* current = head;

	do {
		// if head node is the one to remove
		if (current) {
			if (current->data == data) {
				head = current->next;
				current = NULL;
				free(current);
				break;
			}
		}

		struct node* prev = current;
		current = current->next;
		while (current) {
			if (current->data == data) {
				break;
			}
			prev = current;
			current = current->next;
		}

		// if end of list was reached without finding a match
		if (!current) {
			printf("Could not find value : %d\n", data);
			break;
		}

		// skip over one to be deleted
		prev->next = current->next;
		current = NULL;
		free(current);

	} while (0);
}


int main() {

	insert_at_end(1);
	insert_at_end(2);
	insert_at_end(3);
	insert_at_front(4);

	display();

	remove_node(4);
	remove_node(2);

	display();


	return 0;
	

}

