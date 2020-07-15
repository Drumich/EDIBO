class TodayDateComponent extends HTMLElement {
    constructor(){
        super();
        setInterval(() => {
            this.innerText=new Date();
        }, 1000);     
    }
} 
const comp = customElements.define("todays-date", TodayDateComponent);


// class TodayDateComponent extends HTMLElement {
//     constructor(){
//         super();
//         this.innerText = new Date();                
//     }
// }const comp = customElements.define("todays-date", TodayDateComponent);

        // fetch("https://link to somewhere")
        // .then(j=>j.json())
        // .then(text=>{this.innerText = JSON.stringify(text));
        // });
        // .catch(error => console.error(error));