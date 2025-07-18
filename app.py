from utils import build_ai_prompt, get_ai_suggestions

inflation_percent = int((inflation_rate - 1) * 100)
prompt = build_ai_prompt(location, income, lifestyle, inflation_percent, adjusted)

with st.expander("💡 AI Suggestions"):
    with st.spinner("Generating tips..."):
        tips = get_ai_suggestions(prompt)
        st.markdown(tips)



from utils import format_currency, categorize_budget

# Example use:
st.write(f"Balance: {format_currency(balance)}")
st.info(categorize_budget(balance))
