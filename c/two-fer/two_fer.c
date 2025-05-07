#include "two_fer.h"
#include <string.h>
#include <stdio.h>

void two_fer(char *buffer, const char *name) {
    // Start with "One for "
    strcpy(buffer, "One for ");
    
    // Append name or "you" if name is NULL
    if (name) {
        strcat(buffer, name);
    } else {
        strcat(buffer, "you");
    }
    
    // Append ", one for me."
    strcat(buffer, ", one for me.");
}