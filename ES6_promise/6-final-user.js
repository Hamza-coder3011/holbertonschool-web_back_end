// 6-final-user.js
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)
  ]).then(results => 
    results.map(result => {
      if (result.status === 'fulfilled') {
        return { status: result.status, value: result.value };
      } else {
        // Convert reason to string if it's an Error
        const reason = result.reason instanceof Error ? result.reason.message : result.reason;
        return { status: result.status, value: reason };
      }
    })
  );
}
