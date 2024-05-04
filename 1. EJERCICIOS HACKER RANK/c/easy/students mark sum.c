#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
  //Write your code here.
  int i, sum = 0;
  for(i = 0; i < number_of_students; i++)
  {
	if(gender == 'b')
	{
  		sum += marks[i];
  		i++;
	}
	else
	{
		if(i != number_of_students-1)
		{
			i++;
			sum += marks[i];
		}
  		
	}
  	
  }
  return sum;
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
 	int student;
    for (student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}
