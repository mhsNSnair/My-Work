
function draw() {
  background(50);
//Movement for player
  player.velocity.x =
    (mouseX-player.position.x)*0.055;
  player.velocity.y =
    (mouseY-player.position.y)*0.055;
//physics for player on boxes barriers, boxes on barriers
  player.displace(boxes);
  boxes.displace(boxes);
  boxes.collide(walls1);
  player.collide(walls1);
  boxes.collide(walls2);
  player.collide(walls2);
  boxes.collide(walls3);
  player.collide(walls3);
  boxes.collide(walls4);
  player.collide(walls4);
  boxes.collide(walls5);
  player.collide(walls5);
  boxes.collide(walls6);
  player.collide(walls6);
  boxes.collide(wallsb);
  player.collide(wallsb);
  boxes.collide(wallsb1);
  player.collide(wallsb1);
  boxes.collide(wallsb2);
  player.collide(wallsb2);
  boxes.collide(wallsb3);
  player.collide(wallsb3);



drawSprites();



//if box is over win display win message
    if (boxes.overlap(win) && counter >5){
      noLoop();
      button = createButton('Win!');
      button.mousePressed(winner);
      textSize(200);
      fill(17,90,48);
      text("You Win",250,445);


}

function winner (){

window.open('/Summative/win/index.html');


}




    }
