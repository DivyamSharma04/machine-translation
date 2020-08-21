from textblob import TextBlob
import streamlit as st


st.title("Translate from English to other language")
user_input = st.text_area("write your sentence here")

if st.button("Hindi"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='hi')
	st.write(blob)

if st.button("Chinese"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='zh-CN')
	st.write(blob)

if st.button("French"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='fr')
	st.write(blob)

if st.button("Greek"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='el')
	st.write(blob)

if st.button("Gujarati"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='gu')
	st.write(blob)

if st.button("German"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='de')
	st.write(blob)

if st.button("Italian"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='it')
	st.write(blob)

if st.button("Japanese"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='ja')
	st.write(blob)

if st.button("Punjabi"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='pa')
	st.write(blob)

if st.button("Russian"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='ru')
	st.write(blob)

if st.button("Spanish"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='es')
	st.write(blob)

if st.button("Tamil"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='ta')
	st.write(blob)

if st.button("Urdu"):
	blob = TextBlob(user_input)
	blob = blob.translate(from_lang="en", to='ur')
	st.write(blob)


if __name__ == '__main__':
	main()
