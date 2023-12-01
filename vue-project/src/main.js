import {
    createApp
} from 'vue'
import App from './App.vue'
import router from './router' //라우터 추가
import mixins from './mixins' //믹스인 추가

const app = createApp(App)
app.use(router)
app.mixin(mixins)
app.mount('#app')