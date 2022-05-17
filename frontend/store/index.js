export const getters = {
  isAuthenticated(state) {
    return state.auth.loggedIn
  },

  loggedInUser(state) {
    return state.auth.user
  }
}

export const state = {
  products: [],
  shoppingCart: []
}

export const mutations = {
  addProductToCart(state, liquid){
    // find cartItem
    state.shoppingCart.push(liquid)
    }

  }
