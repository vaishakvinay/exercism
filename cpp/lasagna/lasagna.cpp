// ovenTime returns the amount in minutes that the lasagna should stay in the
// oven.
int ovenTime() {
    
    return 40;
}


int remainingOvenTime(int actualMinutesInOven) {
    
    return ovenTime() - actualMinutesInOven;
}


int preparationTime(int numberOfLayers) {

    return numberOfLayers * 2;
}


int elapsedTime(int numberOfLayers, int actualMinutesInOven) {
    return preparationTime(numberOfLayers) + actualMinutesInOven;
    
}
