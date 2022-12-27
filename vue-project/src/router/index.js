import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DataBinding from '../views/DataBinding.vue'
import DataBindingHtml from '../views/DataBindingHtml.vue'
import DataBindingInputText from '../views/DataBindingInputText.vue'
import DataBindingInputNumber from '../views/DataBindingInputNumber.vue'
import DataBindingTextarea from '../views/DataBindingTextarea.vue'
import DataBindingSelect from '../views/DataBindingSelect.vue'
import DataBindingCheckbox from '../views/DataBindingCheckbox.vue'
import DataBindingCheckbox2 from '../views/DataBindingCheckbox2.vue'
import DataBindingRadio from '../views/DataBindingRadio.vue'
import DataBindingAttribute from '../views/DataBindingAttribute.vue'
import DataBindingButton from '../views/DataBindingButton.vue'
import DataBindingClass from '../views/DataBindingClass.vue'
import DataBindingClass2 from '../views/DataBindingClass2.vue'
import DataBindingStyle from '../views/DataBindingStyle.vue'
import DataBindingStyle2 from '../views/DataBindingStyle2.vue'
import DataBindingList from '../views/DataBindingList.vue'
import RenderingVIf from '../views/RenderingVIf.vue'
import EventClick from '../views/EventClick.vue'
import EventChange from '../views/EventChange.vue'
import Computed_ex from '../views/Computed_ex.vue'
import Watch_ex from '../views/Watch_ex.vue'
import Watch2_ex from '../views/Watch2_ex.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/databinding',
    name: 'DataBinding',
    component: DataBinding
  },
  {
    path: '/databindinghtml',
    name: 'DataBindingHtml',
    component: DataBindingHtml
  },
  {
    path: '/databindinginputtext',
    name: 'DataBindingInputText',
    component: DataBindingInputText
  },
  {
    path: '/databindinginputnumber',
    name: 'DataBindingInputNumber',
    component: DataBindingInputNumber
  },
  {
    path: '/databindingtextarea',
    name: 'DataBindingTextarea',
    component: DataBindingTextarea
  },
  {
    path: '/databindingselect',
    name: 'DataBindingSelect',
    component: DataBindingSelect
  },
  {
    path: '/DataBindingCheckbox',
    name: 'DataBindingCheckbox',
    component: DataBindingCheckbox
  },
  {
    path: '/DataBindingCheckbox2',
    name: 'DataBindingCheckbox2',
    component: DataBindingCheckbox2
  },
  {
    path: '/DataBindingRadio',
    name: 'DataBindingRadio',
    component: DataBindingRadio
  },
  {
    path: '/DataBindingAttribute',
    name: 'DataBindingAttribute',
    component: DataBindingAttribute
  },
  {
    path: '/DataBindingButton',
    name: 'DataBindingButton',
    component: DataBindingButton
  },
  {
    path: '/DataBindingClass',
    name: 'DataBindingClass',
    component: DataBindingClass
  },
  {
    path: '/DataBindingClass2',
    name: 'DataBindingClass2',
    component: DataBindingClass2
  },
  {
    path: '/DataBindingStyle',
    name: 'DataBindingStyle',
    component: DataBindingStyle
  },
  {
    path: '/DataBindingStyle2',
    name: 'DataBindingStyle2',
    component: DataBindingStyle2
  },
  {
    path: '/DataBindingList',
    name: 'DataBindingList',
    component: DataBindingList
  },
  {
    path: '/RenderingVIf',
    name: 'RenderingVIf',
    component: RenderingVIf
  },
  {
    path: '/EventClick',
    name: 'EventClick',
    component: EventClick
  },
  {
    path: '/EventChange',
    name: 'EventChange',
    component: EventChange
  },
  {
    path: '/Computed_ex',
    name: 'Computed_ex',
    component: Computed_ex
  },
  {
    path: '/Watch_ex',
    name: 'Watch_ex',
    component: Watch_ex
  },
  {
    path: '/Watch2_ex',
    name: 'Watch2_ex',
    component: Watch2_ex
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
