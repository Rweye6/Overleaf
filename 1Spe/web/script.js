console.log("Script chargé !");

/*const svg = document.getElementById("mol");

console.log(svg);*/

class Alkane {
    constructor(n){
        this.n = n;
        this.points = [];
        this.branches = [];
    }

    addBranch(position,type){
        this.branches.push({
            position: position,
            type: type
        });
    }

    generatePoints(){
        const dx = 60;
        const dy = 35;

        for(let i=0; i<this.n; i++){
            let x = 60 + i*dx;
            let y = (i%2===0) ? 140 : 140-dy;

            this.points.push({x,y});
        }
    }

    draw(svg){

    this.generatePoints();

    // dessin de la chaîne
    for(let i=0;i<this.points.length-1;i++){
        let p1 = this.points[i];
        let p2 = this.points[i+1]
        
        let line = document.createElementNS( "http://www.w3.org/2000/svg", "line" );
        
        line.setAttribute("x1", p1.x);
        line.setAttribute("y1", p1.y);
        
        line.setAttribute("x2", p2.x);
        line.setAttribute("y2", p2.y);
        
        line.setAttribute("stroke", "black");
        line.setAttribute("stroke-width", "3");
        
        svg.appendChild(line);
    }

    // dessin des carbones
    for(let p of this.points){
        let circle = document.createElementNS( "http://www.w3.org/2000/svg", "circle" );
        circle.setAttribute("cx",p.x);
        circle.setAttribute("cy",p.y);
        circle.setAttribute("r", 4);
        svg.appendChild(circle);
    }

    // dessin des ramifications
    for(let b of this.branches){
        let p = this.points[b.position - 1];
        //liaison verticale
        let line= document.createElementNS( "http://www.w3.org/2000/svg", "line" );
        line.setAttribute("x1", p.x);
        line.setAttribute("y1", p.y);
        line.setAttribute("x2", p.x);
        line.setAttribute("y2", p.y - 50);
        line.setAttribute("stroke", "black");
        line.setAttribute("stroke-width", "2");
        svg.appendChild(line); 
        
        //texte du groupe
        let text = document.createElementNS( "http://www.w3.org/2000/svg", "text" );
        text.setAttribute("x", p.x - 15);
        text.setAttribute("y", p.y - 60);
        text.textContent = b.type;
        svg.appendChild(text);
    }
}
}

const svg1 = document.getElementById("mol1");

let mol1 = new Alkane(7);

mol1.addBranch(2,"CH3");

mol1.draw(svg1);

const svg2 = document.getElementById("mol2");

let mol2 = new Alkane(4);

mol2.addBranch(3,"CH2-CH3");

mol2.draw(svg2);