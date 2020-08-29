import React from 'react'
import './Header.css'
import logo from '../images/logo.png'

import Login from '../Login/Login'

class Header extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            opcoes: ['Como Funciona','Nosso Projeto','Contatos']
        }
    }

    

    render () {
        return (
            <header>
                <img src={logo} alt='Logo' />
                <ul className='listaOpcoes'>
                    {this.state.opcoes.map(opcao => <li className='underline-efect'>{opcao}</li>)}
                </ul>
                < Login />
            </header>
        )
    }
}

export default Header