import React, { Component } from 'react';

class App extends Component{

    constructor(props) {
      super(props);
      this.state = {
        items: [],
        isLoaded: false,

      }

    }

    componentDidMount() {


     fetch('http://localhost:8000/test/load/nile/split')
     .then(res => res.json())
     .then(json => {
       this.setState({
        isLoaded: true,
        items: json,

       })
     });

    }

    render() {

      var { isLoaded, items } = this.state;
      console.log(this.state);
      if (!isLoaded){
        
        return (<div>
          Loading...

        </div> );     
        }

      else {
      return (
        <div className="App">
           <table >
                <tr>
                {items.data.columns.map(item => (
                  <th key={item.id}>{item}</th>
              ))}
                </tr >
                {items.data.data.map(item => (
                  <tr key={item.id}>
                    {item.map(item2 => (
                      <td key={item2.id}>{item2}</td>

                    ))}
                  
                  </tr>
              ))}
                
          </table> 
          
          </div>
        
        );
      }
      

    }


}



export default App;
