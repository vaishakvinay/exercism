#include "darts.h"
#include <math.h>

uint8_t score(coordinate_t landing_position) {
    float d = sqrt(pow(landing_position.x, 2) + pow(landing_position.y, 2));
    if (d <= 1.0f) return 10;
    if (d <= 5.0f) return 5;
    if (d <= 10.0f) return 1;
    
    return 0;
}