(self.webpackChunk=self.webpackChunk||[]).push([[9545],{74248:(e,t,n)=>{n.d(t,{z:()=>l});var i=n(49231),a=n(29375),r=n(85788),o=n.n(r);const l=({onClick:e,variant:t,size:n,width:r,children:l,...g})=>i.createElement("button",{onClick:e,className:(0,a.cs)(o().button,o()[`variant-${t||"primary"}`],o()[`size-${n||"medium"}`],o()[`width-${r||"fixed"}`]),...g},l)},53881:(e,t,n)=>{n.r(t),n.d(t,{GrammarlyBusinessSigninPopup:()=>u});var i=n(49231),a=n(32080),r=n(30302),o=n(21428),l=n(74037),g=n(30916),d=n(29425),s=n(29357),m=n(77634),c=n(74248),p=n(9065);const u=({onShow:e,onHideForToday:t,onClose:n,trackShow:u,authUserDetails:f,isSimpleView:h,...y})=>{const v=d.VP.SignIn,b={source:"authHook",slot:d.G0.Assistant,name:h?d.RP.GBSimpleViewLoginReminder:d.RP.GBLoginReminder,experience:v,lastKnownUserType:(0,g.qf)(f)};return i.useEffect((()=>{u(),(0,l.B0)({...b,userType:f.previousUserType}),h||e()}),[]),i.createElement(m.X,{onClose:n,includeMainContentPadding:!1,headerStyle:{padding:0},mainContent:i.createElement(i.Fragment,null,i.createElement("div",{className:p.gbHeader}),i.createElement(a.k,{direction:"column",gap:2,className:p.gbBody},i.createElement(r.X,{as:"h2",variant:"heading-xsmall"},"You're signed out of Grammarly Business."),h?i.createElement(o.x,{as:"p",variant:"text-small"},"You won't get any writing suggestions until you sign back in."):i.createElement(a.k,{direction:"column",gap:2},i.createElement(o.x,{as:"p",variant:"text-small"},"Sign back in to get"),i.createElement("ul",null,i.createElement("li",null,i.createElement(s.T,{type:"mini",size:18,className:p.logo,ariaHidden:!0}),i.createElement(o.x,{as:"span",variant:"text-small"},"Suggestions that help you write clear, mistake-free text.")),i.createElement("li",{className:p.feedback},i.createElement(o.x,{as:"span",variant:"text-small"},"Feedback that helps you align with your brand's style.")))),i.createElement(a.k,{direction:"column",gap:1,marginTop:3,marginBottom:3},i.createElement(c.z,{onClick:()=>{(0,l.T2)({...b,userType:f.previousUserType,action:v}),y.onSignIn({...b,action:v})},width:"full"},"Sign in"),!h&&i.createElement(c.z,{onClick:t,variant:"tertiary",width:"full",size:"small"},"Don't show this again today."))))})}},85788:e=>{e.exports={button:"EYiE8","variant-primary":"z9uJO","variant-secondary":"q5Jrx","variant-tertiary":"lzg5M","variant-ghost":"a8sQl","size-small":"N98GR","size-medium":"W801A","size-large":"pRgOD","size-xlarge":"UkrPO","width-full":"mw7mz",spin:"PaktZ"}},9065:e=>{e.exports={gbBody:"pwExq",logo:"cnIwI",feedback:"mmSZZ",gbHeader:"JYPij",spin:"R3uJi"}},32080:(e,t,n)=>{n.d(t,{k:()=>l});var i=n(49231),a=n(90199),r=n(31534),o=n(90220);const l=i.forwardRef((function(e,t){const{utility:n,other:a}=(0,r.a)(e),{accessibilityLabel:l,align:d,alignSelf:s,as:m,children:c,className:p,direction:u="row",elevation:f,flex:h,gap:y=0,justify:v,wrap:b=!1,style:x={},...w}=a,R=function({direction:e,wrap:t,elevation:n,className:i,alignSelf:a}){return(0,o.W)("gds-flex","column"===e&&"gds-flex-direction-column",t&&"gds-flex-wrap",n&&`gds-flex-elevation-${n}`,a&&`gds-flex-align-self-${a}`,i)}({direction:u,wrap:b,elevation:f,className:p,alignSelf:s}),k=(0,r.f)(n),E={...g(y),alignItems:d,justifyContent:v,flex:h,...k,...x},T=null!=m?m:"div";return i.createElement(T,{"aria-label":l,ref:t,className:R,style:E,...w},c)}));function g(e){if(null==e)return{};if("number"==typeof e)return{gap:`var(--space-${(0,a.Jy)(e)})`};return{gap:`${null==e.row?"normal":`var(--space-${(0,a.Jy)(e.row)})`} ${null==e.column?"normal":`var(--space-${(0,a.Jy)(e.column)})`}`}}},30302:(e,t,n)=>{n.d(t,{X:()=>o});var i=n(49231),a=n(90220),r=n(90199);const o=i.forwardRef((function(e,t){const{as:n,className:o,variant:l="heading-medium",color:g,align:d,margin:s,marginLeft:m,marginRight:c,marginTop:p,marginBottom:u,style:f,maxLines:h,...y}=e,v={...f,...null!=g&&{color:`var(--color-text-${g})`},...null!=d&&{textAlign:d},...(0,r.AA)({margin:s,marginLeft:m,marginRight:c,marginTop:p,marginBottom:u}),...h&&{WebkitLineClamp:h}};return i.createElement(n,{ref:t,className:(0,a.W)("gds-typography","gds-"+(l.startsWith("heading")?"heading":"text"),`gds-${l}`,h&&"gds-multiline-ellipsis",o),style:v,...y})}))},21428:(e,t,n)=>{n.d(t,{x:()=>o});var i=n(49231),a=n(90220),r=n(90199);const o=i.forwardRef((function(e,t){const{as:n,className:o,variant:l="text-medium",color:d,align:s,weight:m,italic:c,decoration:p,margin:u,marginLeft:f,marginRight:h,marginTop:y,marginBottom:v,style:b,maxLines:x,...w}=e,R={...b,...null!=d&&{color:`var(--color-text-${d})`},...null!=s&&{textAlign:s},...g(m),...null!=c&&{fontStyle:c?"italic":"normal"},...null!=p&&{textDecoration:p},...(0,r.AA)({margin:u,marginLeft:f,marginRight:h,marginTop:y,marginBottom:v}),...x&&{WebkitLineClamp:x}};return i.createElement(n,{ref:t,className:(0,a.W)("gds-typography","gds-"+(l.startsWith("heading")?"heading":"text"),`gds-${l}`,x&&"gds-multiline-ellipsis",o),style:R,...w})})),l={bold:"bold",semibold:600,medium:500,normal:"normal"};function g(e){return null!=e&&l[e]?{fontWeight:l[e]}:null}},54186:(e,t,n)=>{function i(e){if(void 0!==e)return"light-green"===e?"var(--light-green)":"yellow-green"===e?"var(--yellow-green)":/-\d\d?\d?$/.test(e)||"white"===e?`var(--${e})`:`var(--color-${e})`}n.d(t,{y:()=>i})},90199:(e,t,n)=>{function i(e){return.5===e?"half":.25===e?"quarter":`${e}`}function a({margin:e,marginLeft:t,marginRight:n,marginTop:i,marginBottom:a}){const r=l(e);return{marginLeft:o(t,r.left),marginRight:o(n,r.right),marginTop:o(i,r.top),marginBottom:o(a,r.bottom)}}function r({padding:e,paddingLeft:t,paddingRight:n,paddingTop:i,paddingBottom:a}){const r=l(e);return{paddingLeft:o(t,r.left),paddingRight:o(n,r.right),paddingTop:o(i,r.top),paddingBottom:o(a,r.bottom)}}function o(e,t){const n=void 0!==e?e:t;if(void 0!==n){if("string"==typeof n)return n;if(n<0){return`calc(var(--space-${i(-1*n)}) * -1)`}return`var(--space-${i(n)})`}}function l(e){if("string"!=typeof e)return{top:e,right:e,bottom:e,left:e};const t=e.split(" "),n=t[0],i=t[1]||n;return{top:n,right:i,bottom:t[2]||n,left:t[3]||i}}n.d(t,{AA:()=>a,Jy:()=>i,VI:()=>r})},31534:(e,t,n)=>{n.d(t,{a:()=>r,f:()=>o});var i=n(54186),a=n(90199);function r(e){const{bgColor:t,borderColor:n,borderRadius:i,color:a,margin:r,marginLeft:o,marginRight:l,marginTop:g,marginBottom:d,padding:s,paddingLeft:m,paddingRight:c,paddingTop:p,paddingBottom:u,width:f,height:h,...y}=e;return{utility:{bgColor:t,borderColor:n,borderRadius:i,color:a,margin:r,marginLeft:o,marginRight:l,marginTop:g,marginBottom:d,padding:s,paddingLeft:m,paddingRight:c,paddingTop:p,paddingBottom:u,width:f,height:h},other:y}}function o(e){const{bgColor:t,borderColor:n,borderRadius:r,color:o,margin:l,marginLeft:g,marginRight:d,marginTop:s,marginBottom:m,padding:c,paddingLeft:p,paddingRight:u,paddingTop:f,paddingBottom:h,width:y,height:v}=e;return{backgroundColor:(0,i.y)(t),border:void 0!==n?`1px solid var(--color-border-${n})`:void 0,borderRadius:void 0!==r?`var(--radius-${(0,a.Jy)(r)})`:void 0,color:void 0!==o?`var(--color-text-${o})`:void 0,width:"number"==typeof y?`${y}px`:y,height:"number"==typeof v?`${v}px`:v,...(0,a.AA)({margin:l,marginLeft:g,marginRight:d,marginTop:s,marginBottom:m}),...(0,a.VI)({padding:c,paddingLeft:p,paddingRight:u,paddingTop:f,paddingBottom:h})}}}}]);