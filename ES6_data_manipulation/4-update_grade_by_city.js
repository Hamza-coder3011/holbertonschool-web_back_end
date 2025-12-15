export default function updateStudentGradeByCity(students, city, newGrades) {
  // Filter students by city, then map to add grade
  return students
    .filter(student => student.location === city)
    .map(student => {
      const gradeObj = newGrades.find(g => g.studentId === student.id);
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
