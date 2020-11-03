//BASIC SETUP
//set static variables (width, height, svg, g, ax scaling, labels, axis
//get data, include interval function, include update function
//update function: include transition, element join, remove old elements, enter new elements


//DEBUGGING
console.log("Text value:", variable)


//ERRORHANDLING
d3.json("data/ages.json")
	.then(data => {
	<procedure>
}).catch(error => {
	console.log(error)
})


//IF -> THEN -> ELSE
if function
			if (d.name === "Tony") {
				return "blue"
			}
			else {
				return "red"
			}
      
      
//SCALING
const x = d3.scalelinear().domain([1,2]).range([10, 20])
const x = d3.scaleLog().domain([1,200]).range([0, 10]).base(10)
const x = d3.scaleTime().domain([new Date(2000, 0, 1]), new Date(2001, 0, 1)]).range([0, 400])
const x = d3.scaleOrdinal().domain(["a", "b"]).range(["red", "blue"])
const x = d3.scaleBand().domain(["a", "b", "c"]).range([0, 200]).paddingInner(0.3).paddingOuter(0.2)
x.bandwith()


//MIN, MAX, MAP
const min = d3.min(data, d => d.value)
const extent = d3.extent(data, d => d.value) (geeft bereik)
const map = data.map(d => d.<text value column>) (zet text op volgorde)


//INTERVAL
d3.interval(()=> {console.log("testing"}, 1000)


//BOOTSTRAP GRID SYSTEM
<div class='row'>
	<div class='col-xs-12> 12 kolommen voor een klein scherm</div>
</div>
er zijn: col-xs-, col-sm-, col-md-, col-lg-

<div class='row'>
	<div class='col-md-4></div>
	<div class='col-md-4 coll-md-offset-4'> offset van 4 kolommen tov de links naastgelegen kolom</div>
</div>


//D3.JS UPDATE PATTERN
entity.exit().remove()   	  	removes all from screen d3
entity.attr(actions)			updates
entity.enter().append(actions) 	add new


// CODE HINTS
const value = flag ? "profit" : "revenue" (if flag == false then revenue, else profit)



