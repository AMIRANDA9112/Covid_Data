import React, { Component} from 'react';

class Books extends Component {

  state = {
    books: []
  }

  loadBooks = () => {
    fetch('http://127.0.0.1:8000/api/books/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${this.props.token}`
      },
      body: JSON.stringify(this.state.credentials)
    })
    .then( data => data.json())
    .then(
      data => {
        this.setState({books: data})
      }
    )
    .catch( error => console.error(error))
  }

  render() {
    return (
      <div>
        <h2>Select Your Country and Load</h2>

        <h3>At today</h3>

        { this.state.books.map( book => {
          return (
              <h3 key={book.id}>{book.country}</h3>
              )
        })}

        <h4>Confirmed</h4>


        { this.state.books.map( book => {
          return (
              <h3 key={book.id}>{book.infected}</h3>
              )
        })}

        <h4>Recovered</h4>

        { this.state.books.map( book => {
          return (
              <h3 key={book.id}>{book.recovered}</h3>
              )
        })}

        <h4>Death</h4>

        { this.state.books.map( book => {
          return (
              <h3 key={book.id}>{book.deaths}</h3>
              )
        })}

        <button onClick={this.loadBooks}>Load Data</button>
      </div>
    );
  }
}

export default Books;


