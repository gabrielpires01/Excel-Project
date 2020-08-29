import React from 'react'
import './Login.css'

class Login extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            logged: false,
            user: 'Gabriel'
        }
        
        this.onLoggin = this.onLoggin.bind(this)

    }

    onLoggin() {
        let isLogged = this.state.logged;
        this.setState({
            logged: !isLogged
        })
    }

    render() {
        return (
        <div className='login'>
            <h3 className='saudacao'> Bem vindo {this.state.logged ? this.state.user : null}!</h3>
            <button type='button' className='log-button' onClick={this.onLoggin}>
                {this.state.logged ? <span>Log Out</span> : <span>Log In</span>}
            </button>
        </div>
        )
    }
}

export default Login