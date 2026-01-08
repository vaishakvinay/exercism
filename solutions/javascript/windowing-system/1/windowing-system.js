// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */
export function Size(width=80, height=60) {
  this.width = width;
  this.height = height;
 
}

Size.prototype.resize = function(newWidth, newHeight) {
  this.width = newWidth;
  this.height = newHeight;
}
export function Position(x=0, y=0) {
  this.x= x;
  this.y= y;
 
}

Position.prototype.move = function(newX, newY) {
  this.x = newX;
  this.y = newY;
}
export class ProgramWindow {
  constructor() {
    this.screenSize=new Size(800, 600);
    this.size = new Size();
    this.position=new Position();
    
  }

  resize(newSize){
    let width = Math.max(1, newSize.width);
    let height = Math.max(1, newSize.height);
      
    const maxWidth = this.screenSize.width-this.position.x;
    const maxHeight = this.screenSize.height-this.position.y;

    width=Math.min(maxWidth,width);
    height=Math.min(maxHeight,height);

    this.size.width=width;
    this.size.height=height;
  }
move(newPosition){
  const maxX= this.screenSize.width - this.size.width;
  const maxY= this.screenSize.height - this.size.height; 

  let x = Math.min(newPosition.x,maxX);
  let y = Math.min(newPosition.y,maxY);

  x=Math.max(x,0);
  y=Math.max(y,0);


  this.position.move(x,y);
}}
export function changeWindow(programWindow){
  const newSize = new Size(400,300);
  const newPosition= new Position(100,150);

  programWindow.resize(newSize);
  programWindow.move(newPosition);
  
  return programWindow;
}
  

