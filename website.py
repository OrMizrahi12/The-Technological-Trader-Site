import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Technological Trader", layout="wide")

# Background CSS



# --- CSS for Moving Stars Background ---

# --- HEADER ---
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://i.postimg.cc/90nvKZW0/logo.png")  # Your site logo

with col2:


    st.markdown(
        """
        <div style='text-align: right;'>
            <a href='https://wa.me/972502618829' target='_blank' style='margin-right: 15px; outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/vT4VGwdh/whatsapp-logo.png' width='30' style='vertical-align: middle;'>
            </a>
            <a href='mailto:ormizrahi1610@gmail.com' target='_blank' style='margin-right: 15px; outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/Mp3JQkkV/email-logo.png' width='30' style='vertical-align: middle;'>
            </a>
            <a href='https://www.linkedin.com/in/or-mizrahi-yaakov' target='_blank' style='margin-right: 15px; outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/G2QQ4CV1/linkedin-logo.png' width='30' style='vertical-align: middle;'>
            </a>
            <a href='https://www.youtube.com/@TheTechnologicalTrader' target='_blank' style='outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/HLBGCfzV/6.png' width='30' style='vertical-align: middle;'>
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )

 # --- TAGLINE UNDER LOGOS ---

st.markdown(
    """
    <div style='text-align: center; margin-top: 20px; font-size: 20px;'>
        Powerful trading tools for the <span style='font-weight: bold; color: #FF6600;'>Ninjatrader</span> platform
    </div>
    """,
    unsafe_allow_html=True
)


# https://i.postimg.cc/MpQ5Mp5T/Kinetick-Logo.png
st.markdown("---")

st.markdown(
    """
    <div style='display: flex; justify-content: center; align-items: center; gap: 40px;'>
        <a href='https://account.ninjatrader.com/register?introducingPartner=TheTechnologicalTrader' target='_blank' style='text-decoration: none;'>
            <img src='https://i.postimg.cc/kG6S8rfF/Ninja-Trader-Wordmark-color-RGB.png' width='150' style='vertical-align: middle;'>
        </a>
        <a href='http://kinetick.com/NinjaTrader' target='_blank' style='text-decoration: none;'>
            <img src='https://i.postimg.cc/MpQ5Mp5T/Kinetick-Logo.png' width='150' style='vertical-align: middle;'>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")


# THis section needs to show each image in a very power full way! each images contains set of indicators
# that works togheder! 
# Header: Explotr Our cutting edge Trading tools... somting like that
# Footprint image: https://i.postimg.cc/7hxYf03R/Foorprint-Display.png
# Bubbles image: https://i.postimg.cc/rsFM8ccX/Workspaces-1.png
# Price levels image: https://i.postimg.cc/PJ3hJcrL/7.png
# Delta and VWAP: https://i.postimg.cc/PxS0QDG9/image.png

# --- POWERFUL TOOLS SECTION ---

st.markdown("<h2 style='text-align: center; margin-top: 2em;'>Explore Our Cutting-Edge Trading Tools</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; color: gray;'>Unleash your edge with our integrated indicator suites, engineered for maximum trading precision.</p>", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 3em;'></div>", unsafe_allow_html=True)


def powerful_tool(image_url, title, description):
    st.markdown(f"""
        <style>
            .minimal-tool {{
                padding: 50px 0;
                margin-bottom: 3em;
            }}
            .minimal-tool img {{
                width: 100%;
                border-radius: 12px;
                margin-bottom: 20px;
                transition: transform 0.3s ease;
            }}
            .minimal-tool img:hover {{
                transform: scale(1.01);
            }}
            .minimal-tool-title {{
                text-align: center;
                font-size: 1.4em;
                font-weight: 300;
                margin-bottom: 10px;
            }}
            .minimal-tool-description {{
                text-align: center;
                font-size: 1em;
                max-width: 800px;
                margin: 0 auto;
                line-height: 1.6;
            }}
        </style>
        
        <div class="minimal-tool">
            <div class="minimal-tool-title">{title}</div>
            <img src="{image_url}">
            <div class="minimal-tool-description">{description}</div>
        </div>
    """, unsafe_allow_html=True)


# --- IMAGES AND TEXTS ---

with st.expander("Situational Momentum Workspace", True):
    powerful_tool(
        "https://i.postimg.cc/rsFM8ccX/Workspaces-1.png",
        "Situational Momentum Workspace",
        """
        Gain unparalleled real-time insight into current market momentum. 
        The Situational Momentum Workspace empowers traders to instantly recognize aggressive buying and selling activity through dynamic volume bubbles. 
        Spot critical phenomena such as absorption, breakouts, stop runs, orderflow imbalances, momentum bursts, and exhaustion signals with clarity and precision. 
        Designed to keep you locked into the pulse of the market — not lagging behind it.
        """
    )

with st.expander("Intra-Session Orderflow Workspace", False):
    powerful_tool(
        "https://i.postimg.cc/PxS0QDG9/image.png",
        "Intra-Session Orderflow Workspace",
        """
        Master the internal structure of price action across the session. 
        The Intra-Session Orderflow Workspace fuses powerful tools like VWAP dynamics, cumulative delta, 3D momentum models, and trend strength indicators 
        to expose hidden shifts in buying and selling pressure. 
        Stay ahead of institutional activity, track momentum transitions, and read the true story behind every price movement.
        """
    )

with st.expander("Classic Orderflow Workspace", False):
    powerful_tool(
        "https://i.postimg.cc/7hxYf03R/Foorprint-Display.png",
        "Classic Orderflow Workspace",
        """
        Dive deep into the microstructure of the market with professional-grade footprint charts. 
        The Classic Orderflow Workspace reveals the battle between buyers and sellers at every price level, exposing absorption, 
        aggressive pressure, liquidity traps, and hidden divergences. 
        Understand the raw orderflow beneath every candlestick — and position yourself with the smart money, not against it.
        """
    )

with st.expander("Critical Price Levels Workspace", False):
    powerful_tool(
        "https://i.postimg.cc/PJ3hJcrL/7.png",
        "Critical Price Levels Workspace",
        """
        Identify and react to the most strategic price levels with surgical accuracy. 
        The Critical Price Levels Workspace highlights key zones of liquidity, support, resistance, VWAP pivots, and volume clusters — 
        all distilled into an intuitive, easy-to-interpret visual layout. 
        Make faster, smarter trading decisions by always knowing exactly where the market is most vulnerable to shift.
        """
    )


st.markdown("<div style='margin-top: 3em;'></div>", unsafe_allow_html=True)

# --- GALLERY / PRODUCTS ---

products = [
    {
        "image": "https://i.postimg.cc/h4z4kqTK/Screenshot-2025-04-27-084601.png",
        "name": "Bars Coloring Trend",
        "category": "Indicator",
        "description": "Dynamically colors candles based on market momentum and trend strength. Different colors indicate bullish, bearish, or neutral price action to help quickly assess the market environment.",
        "price": "$24.99"
    },
    {
        "image": "https://i.postimg.cc/kMb9jvP4/Screenshot-2025-04-27-085000.png",
        "name": "Bid-Ask Bubbles",
        "category": "Indicator",
        "description": "Visualizes buy and sell volume directly on the price chart by drawing colored bubbles at each bar. Bubble size is proportional to trade volume, helping to quickly spot buying or selling pressure in the market.",
        "price": "$149.99"
    },
    {
        "image": "https://i.postimg.cc/xT3w7sx0/Screenshot-2025-04-27-085529.png",
        "name": "Orderflow Footprint",
        "category": "Indicator",
        "description": "Displays detailed buy and sell volume at each price level within a bar, helping traders analyze market depth, absorption, and imbalance directly inside the candlestick. It reveals the real story behind price movement.",
        "price": "$149.99"
    },
    {
        "image": "https://i.postimg.cc/908GwHXm/Screenshot-2025-04-27-090003.png",
        "name": "VWAP",
        "category": "Indicator",
        "description": "Plots the Volume Weighted Average Price (VWAP) along with dynamic standard deviation bands to visualize fair value zones and potential support/resistance levels throughout the trading session. It also highlights price movement relative to VWAP",
        "price": "$99.99"
    },
    {
        "image": "https://i.postimg.cc/nhtLKwsp/Screenshot-2025-04-27-091121.png",
        "name": "Cumulative Delta",
        "category": "Indicator",
        "description": "Cummelative Delta tracks the ongoing difference between aggressive buying and selling over time, giving a clear view of market pressure shifts. It helps identify hidden strength, weakness, and potential reversals based on order flow dynamics.",
        "price": "$99.99"
    },
    {
        "image": "https://i.postimg.cc/y6MR5jJr/Screenshot-2025-04-27-091416.png",
        "name": "Delta Per Bar",
        "category": "Indicator",
        "description": "Delta measures the real-time difference between aggressive buying and selling within each bar, plotting total, maximum, and minimum delta values. It highlights momentum strength, potential absorption, and hidden shifts in market control.",
        "price": "$99.99"
    },
    {
        "image": "https://i.postimg.cc/FsbY64X7/Screenshot-2025-04-27-091723.png",
        "name": "Cumulative TTG (Transaction Time-gap)",
        "category": "Indicator",
        "description": "Cumulative TTG measures the cumulative time gaps between aggressive buyers and sellers to reveal shifts in trading momentum. It helps detect hidden strength, exhaustion, and imbalances developing beneath price action.",
        "price": "$99.99"
    },
    {
        "image": "https://i.postimg.cc/0jRNtttY/Screenshot-2025-04-27-092029.png",
        "name": "TTG (Transaction Time-gap) Per Bar",
        "category": "Indicator",
        "description": "TTG tracks the time gaps between aggressive buyer and seller transactions, then compares their relative strength to highlight real-time shifts in market momentum. It helps uncover hidden pressure and potential turning points before they show up in price.",
        "price": "$99.99"
    },
    {
        "image": "https://i.postimg.cc/cC0Kmx47/Screenshot-2025-04-27-092939.png",
        "name": "Cumulative TDM (3D Momentum)",
        "category": "Indicator",
        "description": "Cumulative TDM blends transaction timing, price changes, and trade volume into a single momentum signal. It exposes the true balance of buying and selling strength, helping traders detect hidden shifts and potential market reversals early.",
        "price": "$99.99"
    },
    {
        "image": "https://i.postimg.cc/Qt0D2hJJ/Screenshot-2025-04-27-093649.png",
        "name": "TDM (3D Momentum) Per Bar",
        "category": "Indicator",
        "description": "TDM combines transaction timing, price changes, and volume dynamics to reveal the real-time momentum battle between buyers and sellers. It highlights hidden strength shifts and helps traders anticipate market turns before they develop on price charts.",
        "price": "$99.99"
    }
]

st.markdown("<h2 style='text-align: center; margin-top: 2em;'>Our Powerful Indicators</h2>", unsafe_allow_html=True)

cols = st.columns(3)

# for idx, product in enumerate(products):
#     with cols[idx % 3]:
#         st.subheader(product["name"])
#         st.image(product["image"])
#         st.caption(f"**Category:** {product['category']}")
#         st.write(product["description"])
#         st.markdown(f"**Price:** {product['price']}")


for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.subheader(product["name"])
        st.image(product["image"])
        st.caption(f"**Category:** {product['category']}")
        st.write(product["description"])
        st.markdown(f"<span style='color: green; font-weight: bold;'>Price: {product['price']}</span>", unsafe_allow_html=True)

st.markdown("---")

st.header("Who We Are")

st.write(
    """
    At **The Technological Trader**, we specialize in developing advanced strategies, indicators, 
    and powerful add-ons for **NinjaTrader**. 

    We bring a new dimension of power and precision to NinjaTrader platforms by integrating:
    
    - **Advanced Order Flow Analysis**
    - **Momentum-Based Trading Solutions**
    - **Powerful Visualizations and Custom Indicators**

    Our mission is to empower traders with cutting-edge tools that enhance decision-making,
    optimize performance, and unlock the full potential of market insights.

    Join us on your journey to smarter and more effective trading!
    """
)


# --- FOOTER START ---
st.markdown("---")  # Separator line

# --- Disclaimer Section (Full Width) ---
with st.container():
    st.subheader("RISK DISCLOSURE:")
    st.write(
        """
        **Futures and Forex trading contains substantial risk and is not for every investor.
        An investor could potentially lose all or more than the initial investment. 
        Risk capital is money that can be lost without jeopardizing one's financial security or lifestyle.
        Only risk capital should be used for trading and only those with sufficient risk capital should consider trading. 
        Past performance is not necessarily indicative of future results.**

        The information provided by The Technological Trader is for general informational and educational purposes only. 
        All information is provided in good faith; however, we make no representation or warranty of any kind, express or implied, 
        regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information.

        **Trading and Investing Risks**  
        Trading futures, stocks, forex, options, and cryptocurrencies involves substantial risk and is not suitable for every investor. 
        An investor could potentially lose all or more than the initial investment. Risk capital is money that can be lost without 
        jeopardizing one’s financial security or lifestyle. Only risk capital should be used for trading and only those with 
        sufficient risk capital should consider trading.

        **No Financial Advice**  
        All content, tools, indicators, strategies, and techniques provided by us are for educational purposes only and should not 
        be considered financial advice, investment advice, trading advice, or any other advice. We are not a licensed financial 
        advisor, registered investment advisor, or broker-dealer. You should consult with a qualified financial advisor or 
        professional before making any trading or investment decisions.

        **Past Performance**  
        Past performance is not indicative of future results. No representation is being made that any account will or is likely 
        to achieve profits or losses similar to those discussed.

        **Liability**  
        Under no circumstance shall we have any liability to you for any loss or damage of any kind incurred as a result of the use 
        of our information, strategies, indicators, products, or services. Your use of the information and your reliance on any 
        information is solely at your own risk.
        """
    )

# --- Second Row: Logo and Social Links ---
col1, col2 = st.columns([1, 5])

with col1:
    st.image("https://i.postimg.cc/90nvKZW0/logo.png")

with col2:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href='https://wa.me/972502618829' target='_blank' style='margin-right: 15px; outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/vT4VGwdh/whatsapp-logo.png' width='30' style='vertical-align: middle;'>
            </a>
            <a href='mailto:ormizrahi1610@gmail.com' target='_blank' style='margin-right: 15px; outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/Mp3JQkkV/email-logo.png' width='30' style='vertical-align: middle;'>
            </a>
            <a href='https://www.linkedin.com/in/or-mizrahi-yaakov' target='_blank' style='margin-right: 15px; outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/G2QQ4CV1/linkedin-logo.png' width='30' style='vertical-align: middle;'>
            </a>
            <a href='https://www.youtube.com/@TheTechnologicalTrader' target='_blank' style='outline: none; text-decoration: none;'>
                <img src='https://i.postimg.cc/HLBGCfzV/6.png' width='30' style='vertical-align: middle;'>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- FOOTER END ---